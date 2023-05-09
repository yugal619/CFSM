import pytest


@pytest.mark.usefixtures("setup")
class Test_018:

    def test_001(self):
        """Get data by ID from bank"""
        self.shareUtil.bankUtil.get_bank_data_from_id()
