from flask import Blueprint, request, jsonify ,send_file
import csv
from models.restaurant_model import db, Restaurant
from sqlalchemy.exc import IntegrityError

restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@restaurants_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        return jsonify(restaurant.to_dict())
    return jsonify({'message': 'Restaurant not found'}), 404


@restaurants_bp.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    try:
        new_restaurant = Restaurant(
            name=data['name'],
            address=data['address'],
            owner=data['owner'],
            description=data['description'],
            food=data['food']
        )
        db.session.add(new_restaurant)
        db.session.commit()
        return jsonify(new_restaurant.to_dict()), 201
    except KeyError:
        return jsonify({'message': 'Invalid data. Missing required fields'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Restaurant with the same name already exists'}), 400

@restaurants_bp.route('/restaurants/<int:id>', methods=['PUT'])
def update_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'message': 'Restaurant not found'}), 404

    data = request.get_json()
    try:
        restaurant.name = data['name']
        restaurant.address = data['address']
        restaurant.owner = data['owner']
        restaurant.description = data['description']
        restaurant.food = data['food']
        db.session.commit()
        return jsonify(restaurant.to_dict())
    except KeyError:
        return jsonify({'message': 'Invalid data. Missing required fields'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Restaurant with the same name already exists'}), 400

@restaurants_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({'message': 'Restaurant deleted successfully'}), 200
    return jsonify({'message': 'Restaurant not found'}), 404
