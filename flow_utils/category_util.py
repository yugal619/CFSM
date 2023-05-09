
import json
from CFSM.category import Category


class CategoryUtil():

    def __init__(self, base_url, header, log):
        self.base_url = base_url
        self.header = header
        self.log = log
        self.category = Category(self.base_url, self.header)
        self.log.info("category Util is initialized")

    def get_all_category_data(self):
        """Get all categorys data"""
        response = self.category.get_all_category_data()
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        self.log.info(json.dumps(response.json(), indent=3))

        return response

    def get_ids_from_category_data(self):
        """Returns all Id's of categorys"""
        response = self.category.get_all_category_data().json()
        list_of_id = [i['id'] for i in response['data']['data']]
        return list_of_id

    def get_category_data_from_id(self, id=None):
        """Returns data of a category based on ID"""
        if not id:
            id=self.get_ids_from_category_data()[0]
        response = self.category.get_category_data_from_id(id=id)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        return response

    def add_data_in_category(self):
        response = self.category.add_data_in_category()
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'

    def delete_data_in_category(self, categoryId=None):
        if not categoryId:
            categoryId=self.get_ids_from_category_data()[0]
        response = self.category.delete_data_in_category(categoryId)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'

    def update_data_in_category_using_id(self, categoryId=None, **kwargs):
        if not categoryId:
            categoryId = self.get_ids_from_category_data()[0]
        response, request_body = self.category.update_data_in_category_using_id(categoryId, **kwargs)
        assert response.json()['success'] is True, f'[FAILED] Reason - {response.json()["reason"]}'
        response = self.get_category_data_from_id(categoryId).json()['data']['data']
        self.log.info(request_body)
        self.log.info(response)

        keys_to_verify = ['name', 'description']
        for key in keys_to_verify:
            assert response.get(key) == request_body[key], f'[Failure] Value does not match \nActual - ' \
                                                       f'{kwargs[key]} \nExpected {response.get(key)}'
