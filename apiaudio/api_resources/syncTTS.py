from apiaudio.helper_classes import CreatableResource


class SyncTTS(CreatableResource):
    OBJECT_NAME = "SyncTTS"
    resource_path = "/speech/sync"

    @classmethod
    def create(cls, **params):
        headers = {"Accept": "audio/wav"}
        if params.get("format"):
            headers = {"Accept": f"audio/{params.pop('format')}"}
        return cls._post_request(json=params, headers=headers)
