from apiaudio.helper_classes import CreatableResource
from apiaudio.logging import SDKLogger


class SyncTTS(CreatableResource):
    OBJECT_NAME = "SyncTTS"
    resource_path = "/speech/sync"
    logger = SDKLogger(OBJECT_NAME)

    @classmethod
    def create(cls, **params):
        return cls._post_request_raw(json=params, url=f"{cls.resource_path}", istype="wav")
