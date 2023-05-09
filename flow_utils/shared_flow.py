
class SharedUtil():

    def __init__(self, base_url, header, log):
        self.base_url = base_url
        self.header = header
        self.log = log
        self.log.info("Share Util is initialized")

    @property
    def clientUtil(self):
        from flow_utils.client_util import ClientUtil
        return ClientUtil(self.base_url, self.header, self.log)

    @property
    def categoryUtil(self):
        from flow_utils.category_util import CategoryUtil
        return CategoryUtil(self.base_url, self.header, self.log)
