from aflr.helper_classes import (
    CreatableResource,
    DownloadableResource,
    RetrievableResource,
)
import aflr
from aflr.api_request import APIRequest


class Speech(CreatableResource, RetrievableResource, DownloadableResource):
    OBJECT_NAME = "speech"
    resource_path = "/speech"
    file_url = aflr.api_base + "/file/speech"
