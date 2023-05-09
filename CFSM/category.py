from utils.common.request_util import RequestsUtils
from utils.requests_data import request_data
import json
import time

class Category():

    def __init__(self, base_url, header):
        self.base_url = base_url
        self.header = header

    def get_all_category_data(self):
        """Get's all categorys data"""
        uri = '/api/category'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def get_category_data_from_id(self, id):
        """Get categorys data based on ID"""
        uri = f'/api/category/{id}'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def add_data_in_category(self):
        uri = '/api/category'

        random_num = str(int(time.time()))
        body = request_data.add_category_body
        body['name'] += random_num

        response = RequestsUtils.post(host=self.base_url, path=uri, headers=self.header, data=json.dumps(body))
        return response

    def delete_data_in_category(self, categoryId):
        """Get categorys data based on ID"""
        uri = f'/api/category/{categoryId}'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def update_data_in_category_using_id(self, categoryId, **kwargs):
        """
        Updates category data based on categoryId.

        Keyword Args:
        All keyword args supported by update categoryId API.

        Like:-

        name (str, optional): Name of category
        module (str, optional): Module
        """
        uri = f'/api/category/{categoryId}'
        body = request_data.add_category_body
        if kwargs:
            name = kwargs.get("name")
            description = kwargs.get("description")
            if name:
                body["name"] = name
            if description:
                body["description"] = description

        random_num = str(int(time.time()))
        body['name'] += random_num

        response = RequestsUtils.post(host=self.base_url, path=uri, headers=self.header, data=json.dumps(body))
        return response, body
