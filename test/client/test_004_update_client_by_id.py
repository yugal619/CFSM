import pytest


@pytest.mark.usefixtures("setup", "test_setup")
class Test_004:

    @pytest.fixture(scope='function')
    def test_setup(self):
        yield
        self.log.info("Tear down")

    def test_001(self):
        """Update client data by ID"""
        self.shareUtil.clientUtil.update_data_in_client_using_id(type='Newly Updated Type')

    def test_002(self):
        """Update client data by ID"""
        self.shareUtil.clientUtil.update_data_in_client_using_id(name='Newly Updated Name')

    def test_003(self):
        """Update client data by ID"""
        self.shareUtil.clientUtil.update_data_in_client_using_id(phone='Newly Updated phone')

    def test_004(self):
        """Update client data by ID"""
        self.shareUtil.clientUtil.update_data_in_client_using_id(clientId=6, type='Newly Updated Type')

    def test_005(self):
        """Update client data by ID"""
        self.shareUtil.clientUtil.update_data_in_client_using_id(clientId=5)

    def test_006(self):
        """Update client data by ID"""
        self.shareUtil.clientUtil.update_data_in_client_using_id()
