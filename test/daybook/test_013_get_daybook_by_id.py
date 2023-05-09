import pytest


@pytest.mark.usefixtures("setup")
class Test_013:

    def test_001(self):
        """Get data by ID from daybook"""
        self.shareUtil.daybookUtil.get_daybook_data_from_id()
