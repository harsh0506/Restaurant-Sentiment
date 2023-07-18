import re
import string
import nltk
from flask import Flask, request, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

import pickle

app = Flask(__name__)

# Load the pre-trained TF-IDF vectorizer
with open('models/tfidf.pkl', 'rb') as file:
    tfidf = pickle.load(file)

# Load the pre-trained Bernoulli Naive Bayes model
with open('models/bernoulli_model.pkl', 'rb') as file:
    bnb = pickle.load(file)

@app.route('/predict_sentiment', methods=['POST'])
def predict_sentiment():
    try:
        data = request.get_json()
        if 'review' not in data:
            return jsonify({'error': 'Invalid request. "review" field is missing.'}), 400

        review = data['review']
        preprocessed_review = preprocess_review(review)
        tfidf_review = tfidf.transform([preprocessed_review]).toarray()
        sentiment_score = bnb.predict(tfidf_review)[0]

        return jsonify({'sentiment_score': int(sentiment_score)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def preprocess_review(text):
    # Apply the same preprocessing steps as in the 'preprocess_text' function
    text = re.sub(r'<.*?>', '', text)
    text = text.lower()
    text = re.sub(r'http\S+|www\.\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'\d{10}', '', text)
    text = re.sub(r'\bnot\b(\w+)', r'not_\1', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\b\d+\b', '', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in tokens]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

if __name__ == '__main__':
    app.run(debug=True)