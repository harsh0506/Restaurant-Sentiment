from flask import Flask
from models import db
from routes.res_route import restaurants_bp
from routes.cust_route import customers_bp
from routes.review_route import reviews_bp

app = Flask(__name__)

# Load configuration from config.py
app.config.from_object('config.Config')

# Initialize the database
db.init_app(app)

# Register the blueprints
app.register_blueprint(restaurants_bp, url_prefix='/api')
app.register_blueprint(customers_bp, url_prefix='/api')
app.register_blueprint(reviews_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run()
