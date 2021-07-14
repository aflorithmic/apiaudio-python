import apiaudio
from apiaudio.api_request import APIRequest


class File(APIRequest):
    OBJECT_NAME = "file"

    def __init__(self):
        super().__init__()
        self.url = self.api_base + "/file"

    def config_test(self):
        return f"Configured to transact {self.OBJECT_NAME} objects to {self.url} with api_key = {self.api_key}"

    # get speech files
    # TBD

    # get sound files
    # TBD
