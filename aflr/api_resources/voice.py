import aflr
from aflr.api_request import APIRequest


class Voice(APIRequest):
    OBJECT_NAME = "voice"

    def __init__(self):
        super().__init__()
        self.url = self.api_base + "/voice"

    # get voices list
    def list(self):
        return self._get_request(url=self.url)