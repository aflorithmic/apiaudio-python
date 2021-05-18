from aflr.helper_classes import CreatableResource, ListableResource, RetrievableResource


class Script(ListableResource, CreatableResource, RetrievableResource):
    OBJECT_NAME = "script"
    resource_path = "/script"

    def config_test(self):
        return f"Configured to transact {self.OBJECT_NAME} objects to {self.url} with api_key = {self.api_key}"
