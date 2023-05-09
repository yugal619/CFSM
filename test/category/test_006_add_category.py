import pytest


@pytest.mark.usefixtures("setup")
class Test_006:

    def test_006(self):
        """Add data for category"""
        self.shareUtil.categoryUtil.add_data_in_category()
