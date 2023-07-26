from flask_sqlalchemy import SQLAlchemy

from models import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Text)
    food = db.Column(db.Numeric)
    ambience = db.Column(db.Numeric)
    hygiene = db.Column(db.Numeric)
    service = db.Column(db.Numeric)
    sentiment = db.Column(db.Text)
    rid = db.Column(db.Numeric)  # Change column name to 'rid'
    cid = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customeremail = db.Column(db.String(255), nullable=True)
    date = db.Column(db.Date)

    def to_dict(self):
        return {
            'id': self.id,
            'review': self.review,
            'food': self.food,
            'ambience': self.ambience,
            'hygiene': self.hygiene,
            'service': self.service,
            'sentiment': self.sentiment,
            'RId': self.rid,  # Change key name to 'RId'
            'Cid': self.cid,  # Change key name to 'Cid'
            'CustomerEmail': self.customeremail,  # Change key name to 'CustomerEmail'
            'Date': self.date  # Change key name to 'Date'
        }
