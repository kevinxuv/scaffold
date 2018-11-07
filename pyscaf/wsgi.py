# -*- coding: utf-8 -*-
import logging

from flask import Flask, request, jsonify

from pyscaf.core import scaf

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'hello world!'


@app.route('/scaf', methods=['POST'])
def scaffold():
    try:
        data = request.get_json()
        project_root_dir = scaf(**data)
        return jsonify(dict(status=1, data=project_root_dir, error=None))
    except Exception as e:
        logger.exception(e)
        return jsonify(dict(status=0, data=None, error=str(e)))


if __name__ == '__main__':
    app.run()
