import logging
import pytest


@pytest.mark.usefixtures("setup")
class Test_002:

    def test_002(self):
        """Get all data from category"""
        self.shareUtil.clientUtil.get_all_client_data()
