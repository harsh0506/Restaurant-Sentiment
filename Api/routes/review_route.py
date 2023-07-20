from flask import Blueprint, request, jsonify
from models.review_model import Review
from models import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/reviews', methods=['GET'])
def get_reviews():
    try:
        reviews = Review.query.all()
        return jsonify([review.to_dict() for review in reviews])
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@reviews_bp.route('/reviews/<int:id>', methods=['GET'])
def get_review(id):
    try:
        review = Review.query.get(id)
        if review:
            return jsonify(review.to_dict())
        return jsonify({'message': 'Review not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@reviews_bp.route('/reviews', methods=['POST'])
def create_review():
    try:
        data = request.get_json()
        new_review = Review(
            review=data['review'],
            food=data['food'],
            ambience=data['ambience'],
            hygiene=data['hygiene'],
            service=data['service'],
            sentiment=data['sentiment'],
            RId=data['RId'],
            Cid=data['Cid'],
            CustomerEmail=data['CustomerEmail'],
            Date=data['Date']
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201
    except KeyError:
        return jsonify({'message': 'Invalid data provided'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Review with this id already exists'}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@reviews_bp.route('/reviews/<int:id>', methods=['PUT'])
def update_review(id):
    try:
        review = Review.query.get(id)
        if not review:
            return jsonify({'message': 'Review not found'}), 404

        data = request.get_json()
        review.review = data['review']
        review.food = data['food']
        review.ambience = data['ambience']
        review.hygiene = data['hygiene']
        review.service = data['service']
        review.sentiment = data['sentiment']
        review.RId = data['RId']
        review.Cid = data['Cid']
        review.CustomerEmail = data['CustomerEmail']
        review.Date = data['Date']

        db.session.commit()
        return jsonify(review.to_dict())
    except KeyError:
        return jsonify({'message': 'Invalid data provided'}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@reviews_bp.route('/reviews/<int:id>', methods=['DELETE'])
def delete_review(id):
    try:
        review = Review.query.get(id)
        if not review:
            return jsonify({'message': 'Review not found'}), 404

        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'Review deleted successfully'}), 200
    except NoResultFound:
        return jsonify({'message': 'Review not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500
