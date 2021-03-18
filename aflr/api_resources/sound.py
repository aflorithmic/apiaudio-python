import aflr
from aflr.api_request import APIRequest


class Sound(APIRequest):
    OBJECT_NAME = "sound"

    def __init__(self):
        super().__init__()  # add params to the init performed by the base-class
        # good read is https://stackoverflow.com/questions/1385759/should-init-call-the-parent-classs-init
        self.url = self.api_base + "/sound"

    def create(self, **params):
        return self._post_request(url=self.url, json=params)