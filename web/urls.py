from flask import Blueprint
from .controller import *

router = Blueprint("web", __name__)

router.add_url_rule(rule='/', endpoint="web-index", view_func=web_index, methods=['GET'])
router.add_url_rule(rule='/api/get-json-type', endpoint="web-get-mock-data", view_func=get_mock_data, methods=['GET'])
router.add_url_rule(rule='/api/set-json-type', endpoint="web-set-mock-data", view_func=set_mock_data, methods=['GET'])
