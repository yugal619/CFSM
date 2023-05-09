
import json
from CFSM.partner import Partner


class PartnerUtil():

    def __init__(self, base_url, header, log):
        self.base_url = base_url
        self.header = header
        self.log = log
        self.partner = Partner(self.base_url, self.header)
        self.log.info("partner Util is initialized")

    def get_all_partner_data(self):
        """Get all partners data"""
        response = self.partner.get_all_partner_data()
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        self.log.info(json.dumps(response.json(), indent=3))

        return response

    def get_ids_from_partner_data(self):
        """Returns all Id's of partners"""
        response = self.partner.get_all_partner_data().json()
        list_of_id = [i['id'] for i in response['data']['data']]
        return list_of_id

    def get_partner_data_from_id(self, id=None):
        """Returns data of a partner based on ID"""
        if not id:
            id=self.get_ids_from_partner_data()[0]
        response = self.partner.get_partner_data_from_id(id=id)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        return response

    def add_data_in_partner(self):
        response = self.partner.add_data_in_partner()
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'

    def delete_data_in_partner(self, partnerId=None):
        if not partnerId:
            partnerId=self.get_ids_from_partner_data()[0]
        response = self.partner.delete_data_in_partner(partnerId)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'

    def update_data_in_partner_using_id(self, partnerId=None, **kwargs):
        if not partnerId:
            partnerId = self.get_ids_from_partner_data()[0]
        response, request_body = self.partner.update_data_in_partner_using_id(partnerId, **kwargs)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        response = self.get_partner_data_from_id(partnerId).json()['data']['data']

        keys_to_verify = ['account_holder_name', 'partner_name', 'branch_address', 'account_number', 'ifsc_code',
                          'micr_code']
        for key in keys_to_verify:
            assert response.get(key) == request_body[key], f'[Failure] Value does not match \nActual - ' \
                                                       f'{kwargs[key]} \nExpected {response.get(key)}'
