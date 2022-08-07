import logging

from application.clients import RestClient
from upstreams.acl import build_response, build_symbols


logger = logging.getLogger(__name__)


class AlphaVantageClient(RestClient):
    def __init__(self):
        # https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=compact&apikey=X86NOH6II01P7R24
        RestClient.__init__(self, server_url="https://www.alphavantage.co", timeout=30)

    def get(self, symbol):
        query_path = "query?function=TIME_SERIES_DAILY&symbol={}&outputsize=compact&apikey=X86NOH6II01P7R24".format(symbol)
        resp = self.get_request(query_path)
        if resp.status_code != 200:
            logger.error('GET {} \n  Code: {} \n  Detail: {}'.format(query_path, resp.status_code, resp.text))
            return {'message': resp.text}, resp.status_code

        response = build_response(resp.json())
        if not response:
            logger.error('GET {} \n  Code: {} \n  Detail: {}'.format(query_path, resp.status_code, resp.text))
            return {'message': resp.text}, 500

        return response.json(), resp.status_code

    def get_symbols(self):
        query_path = 'query?function=LISTING_STATUS&apikey=X86NOH6II01P7R24'

        resp = self.get_request(query_path)
        if resp.status_code != 200:
            logger.error('GET {} \n  Code: {} \n  Detail: {}'.format(query_path, resp.status_code, resp.text))
            return {'message': resp.text}, resp.status_code

        return build_symbols(resp.content.decode('utf-8')), resp.status_code
