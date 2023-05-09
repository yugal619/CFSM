import pytest


@pytest.mark.usefixtures("setup")
class Test_012:

    def test_001(self):
        """Get all data from daybook"""
        self.shareUtil.daybookUtil.get_all_daybook_data()
