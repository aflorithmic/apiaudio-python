from apiaudio.helper_classes import ListableResource


class Voice(ListableResource):
    OBJECT_NAME = "voice"
    resource_path = "/voice"
    list_parameters_path = "/voice/parameter"

    @classmethod
    def list_parameters(cls):
        return cls._get_request(path_param=cls.list_parameters_path)
