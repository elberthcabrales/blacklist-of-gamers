from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
from services.logger import logger
from configuration.config import config
from routes.blacklist import bp

app = Flask(__name__)

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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['db_url']
db = SQLAlchemy(app)


@app.before_request
def before_request():
    request.logger = logger


app.register_blueprint(bp)

if __name__ == '__main__':
    logger.info(
        "service started at {}:{}".format(
            config['host_service']['host'],
            config['host_service']['port']))
    app.run(host='0.0.0.0', port=5000)
