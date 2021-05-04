import aflr
from aflr.api_request import APIRequest


class Voice(APIRequest):
    OBJECT_NAME = "voice"

    def __init__(self):
        super().__init__()
        self.url = self.api_base + "/voice"
        self.parameters_url = self.api_base + "/voice/parameter"

    # get voices list
    def list(self, **params):
        return self._get_request(url=self.url, request_params=params)

    def list_parameters(self):
        return self._get_request(url=self.parameters_url)