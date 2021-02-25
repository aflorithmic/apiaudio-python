import aflr
from aflr.api_request import APIRequest


class Speech(APIRequest):
    OBJECT_NAME = "speech"

    def __init__(self):
        super().__init__()
        self.url = self.api_base + "/speech"
        self.file_url = self.api_base + "/file/speech"

    def config_test(self):
        return f"Configured to transact {self.OBJECT_NAME} objects to {self.url} with api_key = {self.api_key}"

    # get speech url by scriptId
    def retrieve(self, scriptId):
        return self._get_request(
            url=self.file_url, request_params={"scriptId": scriptId}
        )

    # create a new text-to-speech
    def create(self, **params):
        # params["api"] = False # To be changed when ms-file is ready
        return self._post_request(json=params)

    # download speech files
    def download(self, scriptId, destination="."):
        audio_files = self.retrieve(scriptId)
        local_filenames = []
        print(audio_files)
        for key, value in audio_files.items():
            # Review "value"! list of string...
            local_filename = self._download_request(url=value, destination=destination)
            local_filenames.append(local_filename)

        return local_filenames
