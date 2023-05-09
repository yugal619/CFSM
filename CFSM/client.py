from utils.common.request_util import RequestsUtils
from utils.requests_data import request_data
import json


class Client():

    def __init__(self, base_url, header):
        self.base_url = base_url
        self.header = header

    def get_all_client_data(self):
        """Get's all clients data"""
        uri = '/api/client'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def get_client_data_from_id(self, id):
        """Get clients data based on ID"""
        uri = f'/api/client/{id}'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def add_data_in_client(self):
        uri = '/api/client'
        body = request_data.add_client_body

        response = RequestsUtils.post(host=self.base_url, path=uri, headers=self.header, data=json.dumps(body))
        return response

    def delete_data_in_client(self, clientId):
        """Get clients data based on ID"""
        uri = f'/api/client/{clientId}'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def update_data_in_client_using_id(self, clientId, **kwargs):
        """
        Updates client data based on clientId.

        Keyword Args:
        All keyword args supported by update clientId API.

        Like:-

        type (str, optional): Type of client
        name (str, optional): Name of client
        phone (str, optional): Phone number
        module (str, optional): Module
        """
        uri = f'/api/client/{clientId}'

        if kwargs:
            body = request_data.add_client_body
            type = kwargs.get("type")
            name = kwargs.get("name")
            phone = kwargs.get("phone")
            module = kwargs.get("module")
            if type:
                body["type"] = type
            if name:
                body["name"] = name
            if phone:
                body["phone"] = phone
            if module:
                body["module"] = module

        else:
            body = request_data.update_client_body

        response = RequestsUtils.post(host=self.base_url, path=uri, headers=self.header, data=json.dumps(body))
        return response, body
