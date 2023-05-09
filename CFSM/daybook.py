from utils.common.request_util import RequestsUtils
from utils.requests_data import request_data
import json
import time


class Daybook():

    def __init__(self, base_url, header):
        self.base_url = base_url
        self.header = header

    def get_all_daybook_data(self):
        """Get's all daybooks data"""
        uri = '/api/daybook'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def get_daybook_data_from_id(self, id):
        """Get daybooks data based on ID"""
        uri = f'/api/daybook/{id}'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def add_data_in_daybook(self):
        uri = '/api/daybook'

        body = request_data.add_daybook_body

        response = RequestsUtils.post(host=self.base_url, path=uri, headers=self.header, data=json.dumps(body))
        return response

    def delete_data_in_daybook(self, daybookId):
        """Get daybooks data based on ID"""
        uri = f'/api/daybook/{daybookId}'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def update_data_in_daybook_using_id(self, daybookId, **kwargs):
        """
        Updates daybook data based on daybookId.

        Keyword Args:
        All keyword args supported by update daybookId API.

        Like:-

        name (str, optional): Name of daybook
        module (str, optional): Module
        """
        uri = f'/api/daybook/{daybookId}'
        body = request_data.add_daybook_body
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
