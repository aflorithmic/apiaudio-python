from apiaudio.helper_classes import (
    CreatableResource,
    DownloadableResource,
    ListableResource,
    RetrievableResource,
)


class Sound(
    CreatableResource, DownloadableResource, RetrievableResource, ListableResource
):
    OBJECT_NAME = "sound"
    resource_path = "/sound"
    list_path = "/sound/template"
    file_url = "/file/sound"
    list_parameters_path = "/sound/parameter"

    @classmethod
    def list_parameters(cls):
        return cls._get_request(path_param=cls.list_parameters_path)

    @classmethod
    def list(cls, **args):
        return cls._get_request(path_param=cls.list_path, request_params=args)
