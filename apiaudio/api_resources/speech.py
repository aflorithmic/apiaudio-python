from apiaudio.helper_classes import (
    CreatableResource,
    DownloadableResource,
    RetrievableResource,
)


class Speech(CreatableResource, RetrievableResource, DownloadableResource):
    OBJECT_NAME = "speech"
    resource_path = "/speech"
