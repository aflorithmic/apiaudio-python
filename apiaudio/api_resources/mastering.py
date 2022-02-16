from apiaudio.helper_classes import (
    CreatableResource,
    DownloadableResource,
    RetrievableResource,
)


class Mastering(CreatableResource, RetrievableResource, DownloadableResource):
    OBJECT_NAME = "mastering"
    resource_path = "/mastering"
