import requests
import unittest

class RequestWrapper():

    def __init__(self, server='localhost', port=5000, username=None, password=None):
        self._session = requests.session()
        self._server = server
        self._port = port
        self._username = username
        self._password = password
        self._connected = False
        self._url = 'http://{0}:{1}'.format(server, port)

    @property
    def session(self):
        return self._session

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def server(self):
        return self._server

    @property
    def port(self):
        return self._port

    @property
    def url(self):
        return self._url

    @property
    # do we need this since there's not session???
    def connected(self):
        return self._connected

    def Get(self, route, params=None, data=None, json=None):
        """
        Wrapper around GET method

        :param route: URL path off of server (str)
        :param params:
        :return: result of the GET call (response)
        """
        response = self.session.get('{0}/{1}'.format(self.url, route), params=params, data=data,
                                    json=json)
        return response

    def Options(self, route, params=None, data=None, json=None):
        """
        Wrapper around OPTIONS method

        :param route: URL path off of serer (str)
        :param params: any params to pass (dict)
        :param data: any data to pass (dict)
        :param json: any json to pass (dict)
        :return: result of OPTIONS call (response
        """
        response = self.session.options(f'{self.url}/{route}', params=params, data=data, json=json)
        return response

    def Post(self, route, params=None, data=None, json=None):
        """
        Wrapper around POST method

        :param route: URL path off of the server (str)
        :param params: any params to pass (dict)
        :param data: any data to pass (dict)
        :param json: any json to pass (dict)
        :return: result of the POST call (response)
        """
        response = self.session.post('{0}/{1}'.format(self.url, route), params=params, data=data,
                                     json=json)
        return response

    def Patch(self, route, params=None, data=None, json=None):
        """
        Wrapper around PATCH method

        :param route: URL path off of the server (str)
        :param params:
        :param data:
        :param json:
        :return: result of the PATCH call (response)
        """
        response = self.session.patch('{0}/{1}'.format(self.url, route), params=params, data=data,
                                      json=json)
        return response

    def Delete(self, route, params=None, data=None, json=None):
        """
        Wrapper around the DELETE method

        :param route: URL path off of the server (str)
        :param params:
        :param data:
        :param json:
        :return: result of the DELETE call (response)
        """
        response = self.session.delete('{0}/{1}'.format(self.url, route), params=params, data=data,
                                       json=json)
        return response