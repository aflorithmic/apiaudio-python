from apiaudio.helper_classes import CreatableResource


class SyncTTS(CreatableResource):
    OBJECT_NAME = "SyncTTS"
    resource_path = "/sync_speech/synthesize"
