import aflr
from aflr.api_request import APIRequest


class Sound(APIRequest):
    OBJECT_NAME = "sound"

    def __init__(self):
        super().__init__()  # add params to the init performed by the base-class
        # good read is https://stackoverflow.com/questions/1385759/should-init-call-the-parent-classs-init
        self.url = self.api_base + "/sound"
        self.file_url = self.api_base + "/file/sound"
        self.bg_url = self.api_base + "/file/bg"

    def create(self, **params):
        return self._post_request(url=self.url, json=params)

    def retrieve(self, scriptId, parameters={}):
        parameters.update({"scriptId": scriptId})
        return self._get_request(url=self.file_url, request_params=parameters)

    def list(self):
        return self._get_request(url=self.bg_url)

    def download(self, scriptId, parameters={}, destination="."):
        url = self.retrieve(scriptId=scriptId, parameters=parameters).get("url")
        local_filename = self._download_request(url=url, destination=destination)
        return local_filename
