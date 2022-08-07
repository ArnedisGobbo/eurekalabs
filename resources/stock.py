import logging

from flask import request
from flask_restful import Resource
from application.security import api_required
from upstreams.alphavantage import AlphaVantageClient


logger = logging.getLogger(__name__)


class Stock(Resource):
    @api_required
    def get(self):
        symbol = request.args.get('symbol', default=None, type=str)
        if not symbol:
            logger.error("The symbol cannot be blank.")
            return {'message': "The symbol cannot be blank."}, 400

        upstream = AlphaVantageClient()
        response, status_code = upstream.get_symbols()
        if status_code != 200:
            return response, status_code

        if next(filter(lambda x: x == symbol, response), None) is None:
            logger.error("The symbol '{}' is not active.".format(symbol))
            return {'message': "The symbol '{}' is not active.".format(symbol)}, 400

        response, status_code = upstream.get(symbol)
        if status_code != 200:
            return response, status_code

        logger.info(response)
        return response
