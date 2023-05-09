import pytest


@pytest.mark.usefixtures("setup")
class Test_015:

    def test_001(self):
        """Delete daybook data"""
        self.shareUtil.daybookUtil.delete_data_in_daybook()
