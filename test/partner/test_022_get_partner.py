import pytest


@pytest.mark.usefixtures("setup")
class Test_022:

    def test_001(self):
        """Get all data from partner"""
        self.shareUtil.partnerUtil.get_all_partner_data()
