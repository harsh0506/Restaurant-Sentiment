import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

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

str1 = "<html>harsh you are a. good student ! ,Bigname@noname.com and call me at 9567576910 . </html>"
print("your string : " + str1 , "\n")

print("preprocced text :" + preprocess_review(str1))