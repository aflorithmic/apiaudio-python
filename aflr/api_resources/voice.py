import aflr
from aflr.api_request import APIRequest


class Voice(APIRequest):
    OBJECT_NAME = "voice"

    def __init__(self):
        super().__init__()  # add params to the init performed by the base-class
        # good read is https://stackoverflow.com/questions/1385759/should-init-call-the-parent-classs-init
        self.url = self.api_base + "/voice"

    # get voices list
    def list(self):
        return self._get_request(url=self.url)