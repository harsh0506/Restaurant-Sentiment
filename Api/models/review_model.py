from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text)
    food = db.Column(db.Numeric)
    ambience = db.Column(db.Numeric)
    hygiene = db.Column(db.Numeric)
    service = db.Column(db.Numeric)
    sentiment = db.Column(db.Text)
    RId = db.Column(db.Numeric)
    Cid = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    CustomerEmail = db.Column(db.String(255), nullable=False)
    Date = db.Column(db.Date)

    def to_dict(self):
        return {
            'id': self.id,
            'review': self.review,
            'food': self.food,
            'ambience': self.ambience,
            'hygiene': self.hygiene,
            'service': self.service,
            'sentiment': self.sentiment,
            'RId': self.RId,
            'Cid': self.Cid,
            'CustomerEmail': self.CustomerEmail,
            'Date': self.Date
        }
