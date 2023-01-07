FROM python:3.8

# Install Redis
RUN apt-get update && apt-get install -y redis-server

# Install Flask and other dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the application code
COPY . /app
WORKDIR /app

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# Run the Flask application
CMD ["python", "app.py"]