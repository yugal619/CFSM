import pytest


@pytest.mark.usefixtures("setup")
class Test_018:

    def test_001(self):
        """Get data by ID from partner"""
        self.shareUtil.partnerUtil.get_partner_data_from_id()
