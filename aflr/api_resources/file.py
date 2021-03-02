import aflr
from aflr.api_request import APIRequest


class File(APIRequest):
    OBJECT_NAME = "file"

    def __init__(self):
        super().__init__()
        self.url = self.api_base + "/file"
        self.file_master = self.url + "/mastering"

    def config_test(self):
        return f"Configured to transact {self.OBJECT_NAME} objects to {self.url} with api_key = {self.api_key}"

    # get speech files
    # TBD

    # get sound files
    # TBD

	# get mastering file
	def retrieve_master(self, scriptId, parameters={}):
		parameters.update({'scriptId': scriptId})
		return self._get_request(url=self.file_master, request_params=parameters)

    # download mastering file
	def download_master(self, scriptId, parameters={}, destination="."):
        url = self.retrieve_master(scriptId=scriptId, parameters=parameters)
        url = url if type(url) == str else url.get('url')
        local_filename = self._download_request(url=url, destination=destination) 
        return local_filename
