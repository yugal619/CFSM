import pytest


@pytest.mark.usefixtures("setup", "test_setup")
class Test_019:

    @pytest.fixture(scope='function')
    def test_setup(self):
        yield
        self.log.info("Tear down")

    # def test_014(self):
    #     """Update bank data by ID"""
    #     self.shareUtil.bankUtil.update_data_in_bank_using_id(name='Updated bank Name ')
    #
    # def test_002(self):
    #     """Update bank data by ID"""
    #     self.shareUtil.bankUtil.update_data_in_bank_using_id(description='Updated Description')

    def test_003(self):
        """Update bank data by ID"""
        self.shareUtil.bankUtil.update_data_in_bank_using_id()
