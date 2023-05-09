
import json
from CFSM.bank import Bank


class BankUtil():

    def __init__(self, base_url, header, log):
        self.base_url = base_url
        self.header = header
        self.log = log
        self.bank = Bank(self.base_url, self.header)
        self.log.info("bank Util is initialized")

    def get_all_bank_data(self):
        """Get all banks data"""
        response = self.bank.get_all_bank_data()
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        self.log.info(json.dumps(response.json(), indent=3))

        return response

    def get_ids_from_bank_data(self):
        """Returns all Id's of banks"""
        response = self.bank.get_all_bank_data().json()
        list_of_id = [i['id'] for i in response['data']['data']]
        return list_of_id

    def get_bank_data_from_id(self, id=None):
        """Returns data of a bank based on ID"""
        if not id:
            id=self.get_ids_from_bank_data()[0]
        response = self.bank.get_bank_data_from_id(id=id)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        return response

    def add_data_in_bank(self):
        response = self.bank.add_data_in_bank()
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'

    def delete_data_in_bank(self, bankId=None):
        if not bankId:
            bankId=self.get_ids_from_bank_data()[0]
        response = self.bank.delete_data_in_bank(bankId)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'

    def update_data_in_bank_using_id(self, bankId=None, **kwargs):
        if not bankId:
            bankId = self.get_ids_from_bank_data()[0]
        response, request_body = self.bank.update_data_in_bank_using_id(bankId, **kwargs)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        response = self.get_bank_data_from_id(bankId).json()['data']['data']

        keys_to_verify = ['account_holder_name', 'bank_name', 'branch_address', 'account_number', 'ifsc_code',
                          'micr_code']
        for key in keys_to_verify:
            assert response.get(key) == request_body[key], f'[Failure] Value does not match \nActual - ' \
                                                       f'{kwargs[key]} \nExpected {response.get(key)}'
