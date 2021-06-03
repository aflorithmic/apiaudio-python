from aflr.helper_classes import (
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
    file_url = "/file/sound"
    bg_url = "/file/bg"
    soundtemplates_url = "/file/soundtemplates"

    @classmethod
    def list_sound_templates(cls):
        return cls._get_request(path_param=cls.soundtemplates_url)

    @classmethod
    def list(cls):
        return cls._get_request(path_param=cls.bg_url)