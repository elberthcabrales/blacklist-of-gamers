from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from configuration.config import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['db_url']
db = SQLAlchemy(app)

template = {
    "info": {
        "title": "BLACKLIST",
        "contact": {
            "email": "elberthcabrales@gmail.com",
        },
        "version": "0.0.1"
    },
}
swagger = Swagger(app, template=template)

