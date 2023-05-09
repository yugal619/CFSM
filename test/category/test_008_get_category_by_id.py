import pytest


@pytest.mark.usefixtures("setup")
class Test_008:

    def test_008(self):
        """Get data by ID from category"""
        self.shareUtil.categoryUtil.get_category_data_from_id()
