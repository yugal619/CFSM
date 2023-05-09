import pytest


@pytest.mark.usefixtures("setup")
class Test_007:

    def test_007(self):
        """Get all data from category"""
        self.shareUtil.categoryUtil.get_all_category_data()
