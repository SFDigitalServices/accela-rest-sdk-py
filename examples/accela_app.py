""" Accela app example """
import os
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

    def on_get(self, _req, _resp, name):
        """ on page GET requests """
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
            response = self.accela.records.get_records(record_id, None, 'AccessToken')

            # default
            resp.status = falcon.HTTP_400
            resp.body = json.dumps(jsend.error(response.text))

            # if successful
            if response.status_code == 200:
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(response.json())

        else:
            resp.status = falcon.HTTP_400
            msg = "Parameter ids is required "
            resp.body = json.dumps(jsend.error(msg))
            return
