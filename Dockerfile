# Use the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files into the container
COPY Api ./Api
COPY models ./models
COPY Dockerfile /app
COPY Api/app.py /app
COPY Api/.env /app
COPY Api/config.py /app

# Install the required Python packages
RUN pip install --no-cache-dir flask gunicorn flask-cors pandas nltk python-dotenv psycopg2 aiohttp Flask-SQLAlchemy scikit-learn==1.3.0 flask-cors
RUN pip install gunicorn Flask[async]

# Expose the port on which the Flask app will run (adjust if necessary)
EXPOSE 5000

# Define the command to run your application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
