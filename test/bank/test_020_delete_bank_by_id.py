import pytest


@pytest.mark.usefixtures("setup")
class Test_015:

    def test_001(self):
        """Delete bank data"""
        self.shareUtil.bankUtil.delete_data_in_bank()
