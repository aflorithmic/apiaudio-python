from apiaudio.helper_classes import (
    CreatableResource,
    DownloadableResource,
    RetrievableResource,
)
from apiaudio.logging import SDKLogger


class Speech(CreatableResource, RetrievableResource, DownloadableResource):
    OBJECT_NAME = "speech"
    resource_path = "/speech"
