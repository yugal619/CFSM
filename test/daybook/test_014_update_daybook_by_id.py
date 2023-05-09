import pytest


@pytest.mark.usefixtures("setup", "test_setup")
class Test_014:

    @pytest.fixture(scope='function')
    def test_setup(self):
        yield
        self.log.info("Tear down")

    # def test_014(self):
    #     """Update daybook data by ID"""
    #     self.shareUtil.daybookUtil.update_data_in_daybook_using_id(name='Updated daybook Name ')
    #
    # def test_002(self):
    #     """Update daybook data by ID"""
    #     self.shareUtil.daybookUtil.update_data_in_daybook_using_id(description='Updated Description')

    def test_003(self):
        """Update daybook data by ID"""
        self.shareUtil.daybookUtil.update_data_in_daybook_using_id()
