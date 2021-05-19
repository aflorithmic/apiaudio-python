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