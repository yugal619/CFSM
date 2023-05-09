import pytest


@pytest.mark.usefixtures("setup")
class Test_001:

    def test_001(self):
        """Add data for client"""
        self.shareUtil.clientUtil.add_data_in_client()
