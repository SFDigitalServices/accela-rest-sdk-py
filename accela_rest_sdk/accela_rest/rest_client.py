""" SDK module """
import requests
class AccelaRestClient():
    """ Accela REST Client Class """

    def __init__(self, config):
        self.config = config
        self.config['API_ENDPOINT'] = config.get('BASE_URL', 'https://apis.accela.com')
        self.config['AUTH_ENDPOINT'] = self.config['API_ENDPOINT'] + '/oauth2/token'
        self.config['TOKEN_ENDPOINT'] = self.config['API_ENDPOINT'] + '/oauth2/tokeninfo'

    def get(self, path, params, auth_type):
        """ Get request. """
        url = self.config['API_ENDPOINT'] + path
        headers = self.set_auth_type(auth_type)
        response = requests.get(url, headers=headers, params=params)

        return response

    def post(self, path, data, params, auth_type):
        """ Post request. """
        url = self.config['API_ENDPOINT'] + path
        headers = self.set_auth_type(auth_type)
        response = requests.post(url, headers=headers, data=data, params=params)

        return response

    def set_auth_type(self, auth_type):
        """" Method to set authorization type. """
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        if auth_type == 'AccessToken':
            headers['Authorization'] = self.config.get('ACCESS_TOKEN', '')
        elif auth_type == 'AppCredentials':
            headers['x-accela-appid'] = self.config['APP_ID']
            headers['x-accela-appsecret'] = self.config['APP_SECRET']
        else:
            headers['x-accela-appid'] = self.config['APP_ID']
            headers['x-accela-agency'] = self.config['AGENCY']
            headers['x-accela-environment'] = self.config.get('ENVIRONMENT', '')
        return headers

    def get_token(self, username, password, scope, environment):
        """ Get Token """
        params = {}
        params['grant_type'] = 'password'
        params['client_id'] = self.config['APP_ID']
        params['client_secret'] = self.config['APP_SECRET']
        params['username'] = username
        params['password'] = password
        params['scope'] = scope
        params['agency_name'] = self.config['AGENCY']
        params['environment'] = environment
        url = self.config['AUTH_ENDPOINT']
        headers = {}
        response = requests.post(url, headers=headers, data=params)
        content_json = False
        if response.status_code == 200:
            content_json = response.json()
            self.config['ACCESS_TOKEN'] = content_json['access_token']
            self.config['EXPIRES_IN'] = content_json['expires_in']
            self.config['REFRESH_TOKEN'] = content_json['refresh_token']
            self.config['SCOPE'] = content_json['scope']
        else:
            raise ValueError('get_token.request('+ str(response.status_code) +'):'+response.text)
        return content_json
