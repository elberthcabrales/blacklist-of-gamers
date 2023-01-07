from flask import request
from services.logger import logger
from configuration.config import config
from flask_migrate import Migrate
from core.main import app, db
from routes.blacklist import bp

app.register_blueprint(bp, url_prefix=config['api']['url_prefix'])


@app.before_request
def before_request():
    request.logger = logger


migrate = Migrate(app, db)

if __name__ == '__main__':
    logger.info(
        "service started at {}:{}".format(
            config['host_service']['host'],
            config['host_service']['port']))
    app.run(host='0.0.0.0', port=5000)
