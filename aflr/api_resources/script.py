from aflr.helper_classes import listableResource
import aflr


class Script(listableResource):
    OBJECT_NAME = "script"
    resource_path = "/script"

    def __init__(self):
        print("script")
        super().__init__()  # add params to the init performed by the base-class
        # good read is https://stackoverflow.com/questions/1385759/should-init-call-the-parent-classs-init
        self.url = self.api_base + "/script"

    def config_test(self):
        return f"Configured to transact {self.OBJECT_NAME} objects to {self.url} with api_key = {self.api_key}"

    # get script by scriptId
    def retrieve(self, scriptId):
        return self._get_request(url=self.url, path_param=scriptId)

    # create a new script
    def create(self, **params):
        return self._post_request(json=params)
