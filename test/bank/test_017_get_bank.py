import pytest


@pytest.mark.usefixtures("setup")
class Test_017:

    def test_001(self):
        """Get all data from bank"""
        self.shareUtil.bankUtil.get_all_bank_data()
