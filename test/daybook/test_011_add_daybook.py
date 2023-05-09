import pytest


@pytest.mark.usefixtures("setup")
class Test_011:

    def test_001(self):
        """Add data for Daybook"""
        self.shareUtil.daybookUtil.add_data_in_daybook()
