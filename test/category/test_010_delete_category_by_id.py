import pytest


@pytest.mark.usefixtures("setup")
class Test_010:

    def test_001(self):
        """Delete category data"""
        self.shareUtil.categoryUtil.delete_data_in_category()
