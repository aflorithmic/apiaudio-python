from apiaudio.helper_classes import (
    CreatableResource,
    DownloadableResource,
    RetrievableResource,
)


class CreateMediaTimeline(CreatableResource):
    OBJECT_NAME = "mastering"
    resource_path = "/media-timeline"

class Mastering(CreatableResource, RetrievableResource, DownloadableResource):
    OBJECT_NAME = "mastering"
    resource_path = "/mastering"
    mastering_preset_list_path = resource_path + "-presets"

    loop_status_code = 202

    @classmethod
    def list_presets(cls):
        return cls._get_request(path_param=cls.mastering_preset_list_path)

    @classmethod
    def create_media_timeline(cls, **args):
        return CreateMediaTimeline.create(**args)
    