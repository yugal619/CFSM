import pytest


@pytest.mark.usefixtures("setup", "test_setup")
class Test_009:

    @pytest.fixture(scope='function')
    def test_setup(self):
        yield
        self.log.info("Tear down")

    def test_001(self):
        """Update category data by ID"""
        self.shareUtil.categoryUtil.update_data_in_category_using_id(name='Updated Category Name ')

    def test_002(self):
        """Update category data by ID"""
        self.shareUtil.categoryUtil.update_data_in_category_using_id(description='Updated Description')

    def test_003(self):
        """Update category data by ID"""
        self.shareUtil.categoryUtil.update_data_in_category_using_id()
