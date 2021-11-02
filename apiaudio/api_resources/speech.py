from apiaudio.helper_classes import (
    CreatableResource,
    DownloadableResource,
    RetrievableResource,
)


class Speech(CreatableResource, RetrievableResource, DownloadableResource):
    OBJECT_NAME = "speech"
    resource_path = "/speech"
    sync_tts_path = "/speech/sync"

    @classmethod
    def tts(cls, **params):
        return cls._post_request_raw(json=params, url=f"{cls.sync_tts_path}", istype="wav")
