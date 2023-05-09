from utils.common.request_util import RequestsUtils
from utils.requests_data import request_data
import json
import time


class Partner():

    def __init__(self, base_url, header):
        self.base_url = base_url
        self.header = header

    def get_all_partner_data(self):
        """Get's all partners data"""
        uri = '/api/partner'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def get_partner_data_from_id(self, id):
        """Get partners data based on ID"""
        uri = f'/api/partner/{id}'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def add_data_in_partner(self):
        uri = '/api/partner'

        body = request_data.add_partner_body

        response = RequestsUtils.post(host=self.base_url, path=uri, headers=self.header, data=json.dumps(body))
        return response

    def delete_data_in_partner(self, partnerId):
        """Get partners data based on ID"""
        uri = f'/api/partner/{partnerId}'
        response = RequestsUtils.get(host=self.base_url, path=uri, headers=self.header)
        return response

    def update_data_in_partner_using_id(self, partnerId, **kwargs):
        """
        Updates partner data based on partnerId.

        Keyword Args:
        All keyword args supported by update partnerId API.

        Like:-

        name (str, optional): Name of partner
        module (str, optional): Module
        """
        uri = f'/api/partner/{partnerId}'
        body = request_data.add_partner_body
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
