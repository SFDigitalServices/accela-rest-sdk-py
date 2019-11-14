""" SDK module """
import requests
class SDK():
    """ SDK class """
    def __init__(self, host='https://jsonplaceholder.typicode.com'):
        self.host = host

    def get_url(self, options):
        """ Produce API URL """
        url = self.host + options['path']
        url += '?'
        if 'params' in options and options['params']:
            for key, value in options['params'].items():
                url += '&' + str(key) + '=' + str(value)
        return url

    def get_posts(self, params=None):
        """ Get Posts """
        url = self.get_url({
            'path' : '/posts',
            'params' : params
        })
        posts = []
        response = requests.get(url)
        if response.status_code == 200:
            posts = response.json()
        return posts
