from utils.common.request_util import RequestsUtils
from utils.requests_data import request_data
import json
import time


class Bank():

    def __init__(self, base_url, header):
        self.base_url = base_url
        self.header = header

    def get_all_bank_data(self):
        """Get's all banks data"""
        uri = '/api/bank'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def get_bank_data_from_id(self, id):
        """Get banks data based on ID"""
        uri = f'/api/bank/{id}'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def add_data_in_bank(self):
        uri = '/api/bank'

        body = request_data.add_bank_body

        response = RequestsUtils.post(host=self.base_url, path=uri, headers=self.header, data=json.dumps(body))
        return response

    def delete_data_in_bank(self, bankId):
        """Get banks data based on ID"""
        uri = f'/api/bank/{bankId}'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def update_data_in_bank_using_id(self, bankId, **kwargs):
        """
        Updates bank data based on bankId.

        Keyword Args:
        All keyword args supported by update bankId API.

        Like:-

        name (str, optional): Name of bank
        module (str, optional): Module
        """
        uri = f'/api/bank/{bankId}'
        body = request_data.add_bank_body
        if kwargs:
            name = kwargs.get("name")
            description = kwargs.get("description")
            if name:
                body["name"] = name
            if description:
                body["description"] = description

        # random_num = str(int(time.time()))
        # body['name'] += random_num

        response = RequestsUtils.post(host=self.base_url, path=uri, headers=self.header, data=json.dumps(body))
        return response, body
