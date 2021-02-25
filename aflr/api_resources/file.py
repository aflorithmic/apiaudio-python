import aflr
from aflr.api_request import APIRequest

class File(APIRequest):
	OBJECT_NAME = "file"

	def __init__(self):
		super().__init__() # add params to the init performed by the base-class
		# good read is https://stackoverflow.com/questions/1385759/should-init-call-the-parent-classs-init
		self.url = self.api_base + "/file"

	def config_test(self):
		return f"Configured to transact {self.OBJECT_NAME} objects to {self.url} with api_key = {self.api_key}"

	# get speech files
	# TBD

	# get sound files
	# TBD

	# get mastering fiels 
	# TBD