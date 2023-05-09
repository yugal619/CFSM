
import json
from CFSM.client import Client


class ClientUtil():

    def __init__(self, base_url, header, log):
        self.base_url = base_url
        self.header = header
        self.log = log
        self.client = Client(self.base_url, self.header)
        self.log.info("Client Util is initialized")

    def get_all_client_data(self):
        """Get all clients data"""
        response = self.client.get_all_client_data()
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        self.log.info(json.dumps(response.json(), indent=3))

        return response

    def get_ids_from_client_data(self):
        """Returns all Id's of clients"""
        response = self.client.get_all_client_data().json()
        list_of_id = [i['id'] for i in response['data']['data']]
        return list_of_id

    def get_client_data_from_id(self, id=None):
        """Returns data of a client based on ID"""
        if not id:
            id=self.get_ids_from_client_data()[0]
        response = self.client.get_client_data_from_id(id=id)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        return response

    def add_data_in_client(self, **kwargs):
        response = self.client.add_data_in_client(**kwargs)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'

    def delete_data_in_client(self, clientId=None):
        if not clientId:
            clientId=self.get_ids_from_client_data()[0]
        response = self.client.delete_data_in_client(clientId)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'

    def update_data_in_client_using_id(self, clientId=None, **kwargs):
        if not clientId:
            clientId = self.get_ids_from_client_data()[0]
        response, request_body = self.client.update_data_in_client_using_id(clientId, **kwargs)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        response = self.get_client_data_from_id(clientId).json()['data']['data']

        keys_to_verify = ['type', 'name', 'phone']
        for key in keys_to_verify:
            assert response.get(key) == request_body[key], f'[Failure] Value does not match \nActual - ' \
                                                       f'{kwargs[key]} \nExpected {response.get(key)}'
