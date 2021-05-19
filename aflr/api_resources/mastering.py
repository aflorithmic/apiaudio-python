import aflr
from aflr.helper_classes import (
    CreatableResource,
    DownloadableResource,
    RetrievableResource,
)


class Mastering(CreatableResource, RetrievableResource, DownloadableResource):
    OBJECT_NAME = "mastering"
    resource_path = "/mastering"
    file_url = "/file/mastering"

    # download mastering file
    def download(self, scriptId, parameters={}, destination="."):
        url = self.retrieve(scriptId=scriptId, parameters=parameters).get("url")
        if not url:
            raise Exception(
                "Error: No mastered files found. Please try again in a few seconds."
            )
        local_filename = self._download_request(url=url, destination=destination)
        return local_filename