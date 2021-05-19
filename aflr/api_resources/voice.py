from aflr.helper_classes import ListableResource
import aflr


class Voice(ListableResource):
    OBJECT_NAME = "voice"
    resource_path = "/voice"
    parameters_url = aflr.api_base + "/voice/parameter"

    @classmethod
    def list_parameters(cls):
        return cls._get_request(url=cls.parameters_url)