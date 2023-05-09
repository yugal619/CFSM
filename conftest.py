import pytest
import json
import logging
from faker import Faker
from utils.header import header_data
from utils.requests_data import request_data
from flow_utils.shared_flow import SharedUtil
from utils.common.request_util import RequestsUtils


with open("/Ayush/env_config/qa.json") as f:
    data = json.load(f)


@pytest.fixture(scope='class')
def setup(request, set_authentication):
    logging.info('Initializing objects')
    request.cls.BASE_URL = 'http://52.22.123.139'
    request.cls.header = header_data.get_header()
    request.cls.header['Authorization'] = set_authentication
    logging.info(request.cls.header)
    request.cls.fake = Faker()
    request.cls.log = logging.getLogger()
    request.cls.shareUtil = SharedUtil(base_url=request.cls.BASE_URL, header=request.cls.header, log=request.cls.log)


@pytest.fixture(scope='session')
def set_authentication(request):

    logging.info("Generating Auth Token")
    # Check whether user is already registered, if user is registered then authentication token is generated
    # otherwise if user already exists then authorization token will be generated by logging in user

    base_url = data["base_url"]
    path = '/api/register'
    response = RequestsUtils.post(host=base_url, path=path, headers=header_data.get_header(),
                             data=json.dumps(request_data.register_new_user_body))
    response_data = response.json()
    if response_data['success'] is True:
        token = response_data['data']['data']['token']
        logging.info('Token generated by registering new user')
    else:
        path = '/api/login'
        response = RequestsUtils.post(host=base_url, path=path, headers=header_data.get_header(),
                                        data=json.dumps(request_data.login_body))
        response_data = response.json()
        token = response_data['data']['data']['token']
        logging.info('Token generated by logging in existing user')

    yield ' '.join(['Bearer', token])
