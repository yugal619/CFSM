
import json
from CFSM.daybook import Daybook


class DaybookUtil():

    def __init__(self, base_url, header, log):
        self.base_url = base_url
        self.header = header
        self.log = log
        self.daybook = Daybook(self.base_url, self.header)
        self.log.info("daybook Util is initialized")

    def get_all_daybook_data(self):
        """Get all daybooks data"""
        response = self.daybook.get_all_daybook_data()
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        self.log.info(json.dumps(response.json(), indent=3))

        return response

    def get_ids_from_daybook_data(self):
        """Returns all Id's of daybooks"""
        response = self.daybook.get_all_daybook_data().json()
        list_of_id = [i['id'] for i in response['data']['data']]
        return list_of_id

    def get_daybook_data_from_id(self, id=None):
        """Returns data of a daybook based on ID"""
        if not id:
            id=self.get_ids_from_daybook_data()[0]
        response = self.daybook.get_daybook_data_from_id(id=id)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        return response

    def add_data_in_daybook(self):
        response = self.daybook.add_data_in_daybook()
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'

    def delete_data_in_daybook(self, daybookId=None):
        if not daybookId:
            daybookId=self.get_ids_from_daybook_data()[0]
        response = self.daybook.delete_data_in_daybook(daybookId)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'

    def update_data_in_daybook_using_id(self, daybookId=None, **kwargs):
        if not daybookId:
            daybookId = self.get_ids_from_daybook_data()[0]
        response, request_body = self.daybook.update_data_in_daybook_using_id(daybookId, **kwargs)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        response = self.get_daybook_data_from_id(daybookId).json()['data']['data']

        keys_to_verify = ['client_id', 'task_type', 'category_id', 'subcategory_id', 'fees', 'advance', 'balance',
                          'remark', 'employee_id', 'start_date', 'end_date', 'priority']
        for key in keys_to_verify:
            assert response.get(key) == request_body[key], f'[Failure] Value does not match \nActual - ' \
                                                       f'{kwargs[key]} \nExpected {response.get(key)}'
