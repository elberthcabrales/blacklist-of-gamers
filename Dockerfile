FROM python:3.8

# Install Redis
RUN apt-get update

# Install Flask and other dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the application code
COPY . /app
WORKDIR /app

# Run the Flask application
CMD ["python", "app.py"]