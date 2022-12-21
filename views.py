from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from db import db
from models import RequestParamsSchema
from utils import build_query

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        params = RequestParamsSchema().load(request.json)
    except ValidationError as error:
        return error.messages, '400'

    result = None
    for query in params['queries']:
        result = build_query(
            cmd=query['cmd'],
            param=query['value'],
            filename=params['filename'],
            data=result
        )

    return jsonify(result), '200'


@main_bp.route('/test_db')
def test_db():
    result = db.session.execute(
        '''
        SELECT 1
        '''
    ).scalar()

    return jsonify(
        {
            'result': result,
        }
    )
