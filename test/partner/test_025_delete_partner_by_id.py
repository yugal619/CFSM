import pytest


@pytest.mark.usefixtures("setup")
class Test_025:

    def test_001(self):
        """Delete partner data"""
        self.shareUtil.partnerUtil.delete_data_in_partner()
