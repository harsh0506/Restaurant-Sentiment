# Use the official Python base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY Api/requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code to the container
COPY api/ app/
COPY models/ models/

# Expose the Flask app port
EXPOSE 5000

# Set environment variables (Optional: You can load .env at runtime instead)
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV DOTENV_PATH=api/.env

# Run the Flask app using Gunicorn as the WSGI server
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
