import pytest


@pytest.mark.usefixtures("setup")
class Test_003:

    def test_003(self):
        """Get data by ID from category"""
        self.shareUtil.clientUtil.get_client_data_from_id()
