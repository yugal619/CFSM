import pytest


@pytest.mark.usefixtures("setup")
class Test_016:

    def test_001(self):
        """Add data for bank"""
        self.shareUtil.bankUtil.add_data_in_bank()
