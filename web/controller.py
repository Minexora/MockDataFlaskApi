from flask import request
from flask import jsonify
from config.conf import Config

conf_cls = Config()
config = conf_cls()


def web_index():
    return jsonify({"status": 200, "msg": "Sunucu Çalışıyor..."})


def get_mock_data():
    try:
        json_type = request.json.get('type')
        if (json_type in config['file_config']):
            return jsonify({"status": 200, "data": config['file_config'][json_type]})
        else:
            return jsonify({"status": 400, "msg": "Json type bulunamadı."})
    except Exception as e:
        return jsonify({"status": 400, "msg": str(e)})


def set_mock_data():
    try:
        json_type = request.json.get('type')
        content = request.json.get('content')
        config['file_config'][json_type] = content
        conf_cls.print_json_file(config=config)
        return jsonify({"status": 200, "msg": "Mock data başarıyla kaydedildi."})
    except Exception as e:
        return jsonify({"status": 400, "msg": str(e)})
