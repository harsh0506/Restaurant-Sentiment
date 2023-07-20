from flask import Blueprint, request, jsonify
from models.customer_model import Customer
from models import db
from sqlalchemy.exc import IntegrityError

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers])

@customers_bp.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get(id)
    if customer:
        return jsonify(customer.to_dict())
    return jsonify({'message': 'Customer not found'}), 404

@customers_bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_customer)
    try:
        db.session.commit()
        return jsonify(new_customer.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Customer with this email already exists'}), 400

@customers_bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404

    data = request.get_json()
    customer.name = data['name']
    customer.email = data['email']
    customer.phone = data['phone']

    db.session.commit()
    return jsonify(customer.to_dict())

@customers_bp.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get(id)
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404

    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted successfully'}), 200
