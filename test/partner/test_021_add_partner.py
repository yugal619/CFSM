import pytest


@pytest.mark.usefixtures("setup")
class Test_021:

    def test_001(self):
        """Add data for partner"""
        self.shareUtil.partnerUtil.add_data_in_partner()
