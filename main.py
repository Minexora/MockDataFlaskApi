import os
from flask import Flask
from flask_cors import CORS
from config.conf import Config
from web.urls import router as web_router

conf_cls = Config()
config = conf_cls()

app = Flask(__name__, static_folder="static")

CORS(app)

app.register_blueprint(web_router, url_prefix="/")

if __name__ == "__main__":    
    app.run(host=config['env_config']['FLASK_HOST'],port=config['env_config']['FLASK_PORT'])