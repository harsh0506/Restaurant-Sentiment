from flask import Blueprint, request, jsonify, send_file
from models.review_model import Review, db
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound
import re
import pandas as pd
import string
import nltk
import os
from flask import Flask, request, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from sqlalchemy.orm import load_only
import time

import asyncio

import pickle

reviews_bp = Blueprint('reviews', __name__)

# Load the pre-trained TF-IDF vectorizer
with open('C:\\Users\\sneah\\Python projects\\Sentiment nalysis\\models\\tfidf.pkl', 'rb') as file:
    tfidf = pickle.load(file)

# Load the pre-trained Bernoulli Naive Bayes model
with open('C:\\Users\\sneah\\Python projects\\Sentiment nalysis\\models\\bernoulli_model.pkl', 'rb') as file:
    bnb = pickle.load(file)


def preprocess_review(text):
    # Remove HTML tags and convert to lowercase
    text = re.sub(r'<.*?>', '', text)
    text = text.lower()

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords and perform stemming and lemmatization
    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    tokens = [
        lemmatizer.lemmatize(stemmer.stem(word), get_wordnet_pos(word))
        for word in tokens
        if word not in stop_words and word not in string.punctuation and not word.isdigit()
    ]

    preprocessed_text = ' '.join(tokens)
    return preprocessed_text


def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN,
                "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)


@reviews_bp.route('/reviews', methods=['GET'])
async def get_reviews():
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


def convert_sql_output(sql_output):
    results = {}
    for row in sql_output:
        column, value, count = row
        if column not in results:
            results[column] = []
        results[column].append({
            'count': count,
            'rating': int(value)
        })

    return results


@reviews_bp.route("/getResSpecificData/<int:rid>", methods=["GET"])
async def get_res_details(rid):
    raw_sql_query = f'''SELECT
    'ambience' AS column_name,
    ambience AS value,
    COUNT(*) AS count
FROM
    review
WHERE
    ambience >= 1 AND ambience <= 5
    AND rid = {rid}
GROUP BY
    column_name, value

UNION ALL

SELECT
    'food' AS column_name,
    food AS value,
    COUNT(*) AS count
FROM
    review
WHERE
    food >= 1 AND food <= 5
    AND rid = {rid}
GROUP BY
    column_name, value

UNION ALL

SELECT
    'service' AS column_name,
    service AS value,
    COUNT(*) AS count
FROM
    review
WHERE
    service >= 1 AND service <= 5
    AND rid = {rid}
GROUP BY
    column_name, value
    
UNION ALL 

SELECT
    'hygiene' AS column_name,
    service AS value,
    COUNT(*) AS count
FROM
    review
WHERE
    service >= 1 AND service <= 5
    AND rid = {rid}
GROUP BY
    column_name, value

ORDER BY
    column_name, value; '''
    res = convert_sql_output(db.session.execute(raw_sql_query).fetchall())

    result = db.session.query(
        func.avg(Review.hygiene).label('average_hygiene'),
        func.avg(Review.food).label('average_food'),
        func.avg(Review.service).label('average_service'),
        func.avg(Review.ambience).label('average_ambience')
    ).filter((Review.rid == rid)).first()

    return jsonify(res, {"average_hygiene": result.average_hygiene,
                         "average_food": result.average_food,
                         "average_service": result.average_service,
                         "average_ambience": result.average_ambience})


@reviews_bp.route("/sentiment", methods=["POST"])
async def Get_sentiment():
    try:
        data = request.get_json()
        preprocessed_review = preprocess_review(data['review'])
        tfidf_review = tfidf.transform([preprocessed_review]).toarray()
        sentiment_score = bnb.predict(tfidf_review)[0]

        return jsonify({"score": str(sentiment_score), "review": data["review"]}), 201

    except KeyError:
        return jsonify({'message': 'Invalid data provided'}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@reviews_bp.route('/reviews', methods=['POST'])
async def create_review():
    try:
        data = request.get_json()
        new_review = Review(
            review=data['review'],
            food=data['food'],
            ambience=data['ambience'],
            hygiene=data['hygiene'],
            service=data['service'],
            rid=data['RId'],
            cid=data['Cid'],
            customeremail=data.get('CustomerEmail', ''),
            date=data['Date']
        )

        # Preprocess the review text
        preprocessed_review = preprocess_review(data['review'])
        tfidf_review = tfidf.transform([preprocessed_review]).toarray()
        sentiment_score = bnb.predict(tfidf_review)[0]
        new_review.sentiment = str(sentiment_score)

        # Add the review to the session without committing yet
        db.session.add(new_review)

        try:
            # Commit the batch of reviews to the database
            db.session.commit()
        except IntegrityError:
            # Rollback in case of any integrity errors
            db.session.rollback()
            return jsonify({'message': 'Review with this id already exists'}), 400

        return jsonify(new_review.to_dict()), 201

    except KeyError:
        return jsonify({'message': 'Invalid data provided'}), 400
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
