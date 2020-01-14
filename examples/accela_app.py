""" Accela app example """
import os
import sys
import json
import falcon
import jsend
from accela_rest_sdk.accela import Accela

def run():
    """ run function"""
    api = falcon.API()
    api.add_route('/page/{name}', Page())
    api.add_sink(Page().default_error, '')
    return api

class Page():
    """ Page class """
    accela = None

    def on_get(self, req, resp, name):
        """ on page GET requests """
        self.dispatch(req, resp, name)

    def on_post(self, req, resp, name):
        """ on page POST requests """
        self.dispatch(req, resp, name)

    def on_put(self, req, resp, name):
        """ on page POST requests """
        self.dispatch(req, resp, name)

    def dispatch(self, _req, _resp, name):
        """ Dispatch requests """
        dispatch = None
        if hasattr(self.__class__, name) and callable(getattr(self.__class__, name)):
            dispatch = getattr(self, name)
            config = {}
            config['APP_ID'] = os.environ.get('ACCELA_APP_ID')
            config['APP_SECRET'] = os.environ.get('ACCELA_APP_SECRET')
            config['AGENCY'] = os.environ.get('ACCELA_AGENCY')

            self.accela = Accela(config)

            environment = os.environ.get('ACCELA_ENVIRONMENT')
            username = os.environ.get('ACCELA_USERNAME')
            password = os.environ.get('ACCELA_PASSWORD')
            scope = os.environ.get('ACCELA_SCOPE')

            self.accela.client.get_token(username, password, scope, environment)
        else:
            dispatch = self.default_page
        dispatch(_req, _resp)

    def default_page(self, _req, _resp):
        # pylint: disable=no-self-use
        """ default page response """
        msg = {'message': 'hello'}
        _resp.body = json.dumps(jsend.success(msg))
        _resp.status = falcon.HTTP_200

    def default_error(self, _req, resp):
        # pylint: disable=no-self-use
        """Handle default error"""
        msg = falcon.HTTP_404
        status = falcon.HTTP_404
        resp.status = status
        msg_error = jsend.error(msg)
        resp.body = json.dumps(msg_error)

    def get_records(self, req, resp):
        """ example get_records response """
        if 'ids' in req.params:
            record_id = req.params['ids']
            params = req.params
            del params['ids']

            response = self.accela.records.get_records(record_id, params, 'AccessToken')

            # default
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(jsend.error(response.text))

            # if successful
            if response.status_code == 200:
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(response.json())

        else:
            resp.status = falcon.HTTP_400
            msg = "Parameter ids is required"
            resp.body = json.dumps(jsend.error(msg))
            return

    def create_record(self, req, resp):
        """ example create_record """
        if req.content_length:
            params = {'fields':'customId,id'}
            record = req.stream.read(sys.maxsize)
            response = self.accela.records.create_record(record, params)

            # default
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(jsend.error(response.text))

            # if successful
            if response.status_code == 200:
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(response.json())

        else:
            resp.status = falcon.HTTP_400
            msg = "The create record information is missing"
            resp.body = json.dumps(jsend.error(msg))
            return

    def update_record_custom_tables(self, req, resp):
        """ example update_record_custom_tables """
        record_ids = None
        if 'ids' in req.params:
            record_ids = req.params['ids']

        if not record_ids:
            resp.status = falcon.HTTP_400
            msg = "The ID of the record to fetch is missing"
            resp.body = json.dumps(jsend.error(msg))
            return

        if req.content_length:
            params = req.params
            del params['ids']

            custom_tables = req.stream.read(sys.maxsize)
            response = self.accela.records.update_record_custom_tables(
                record_ids, custom_tables, params)

            # default
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(jsend.error(response.text))

            # if successful
            if response.status_code == 200:
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(response.json())

        else:
            resp.status = falcon.HTTP_400
            msg = "Request body is required."
            resp.body = json.dumps(jsend.error(msg))
            return
