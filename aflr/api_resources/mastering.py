import aflr
from aflr.api_request import APIRequest


class Mastering(APIRequest):
    OBJECT_NAME = "mastering"

    def __init__(self):
        super().__init__()
        self.file_url = self.api_base + "/file/mastering"
        self.mastering_url = self.api_base + "/mastering"

    def config_test(self):
        return f"Configured to transact {self.OBJECT_NAME} objects to {self.url} with api_key = {self.api_key}"

    def request(self, scriptId, backgroundTrackId, audience=[]):
        if type(audience) != list:
            raise Exception("audience needs to be a list.")
        if type(backgroundTrackId) != str:
            raise Exception("backgroundTrackId needs to be a string.")
        if type(scriptId) != str:
            raise Exception("scriptId needs to be a string.")
        body = {
            "scriptId": scriptId,
            "backgroundTrackId": backgroundTrackId,
            "audience": audience,
        }
        return self._post_request(url=self.mastering_url, json=body)

    # get mastering file
    def retrieve(self, scriptId, parameters={}):
        parameters.update({"scriptId": scriptId})
        return self._get_request(url=self.file_url, request_params=parameters)

    # download mastering file
    def download(self, scriptId, parameters={}, destination="."):
        url = self.retrieve(scriptId=scriptId, parameters=parameters).get("url")
        local_filename = self._download_request(url=url, destination=destination)
        return local_filename
