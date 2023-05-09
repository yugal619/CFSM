import pytest


@pytest.mark.usefixtures("setup")
class Test_005:

    def test_001(self):
        """Delete client data"""
        self.shareUtil.clientUtil.delete_data_in_client()
