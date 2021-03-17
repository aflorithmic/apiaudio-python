import aflr
from aflr.api_request import APIRequest


class SyncTTS(APIRequest):
    OBJECT_NAME = "sync_tts"

    def __init__(self):
        super().__init__()
        self.url = self.api_base + "/sync_speech/synthesize"

    def config_test(self):
        return f"Configured to transact {self.OBJECT_NAME} objects to {self.url} with api_key = {self.api_key}"

    # create a new text-to-speech
    def create(self, **params):
        return self._post_request(json=params)

