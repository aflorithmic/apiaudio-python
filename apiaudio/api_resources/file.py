from apiaudio.helper_classes import UploadableResource


class File(UploadableResource):
    audio_resource_path = "/file/customaudio/"
    OBJECT_NAME = "file"
    resource_path = "/file"

    @classmethod
    def get_download_url(cls, mediaId):
        return cls._get_request(
            path_param=cls.audio_resource_path + "mediaid?",
            request_params={"mediaId": mediaId},
        )

    @classmethod
    def list(cls, tags=None):
        if tags:
            return cls._get_request(
                path_param=cls.audio_resource_path + "tags?",
                request_params={"tags": tags},
            )
        return cls._get_request(path_param=cls.audio_resource_path + "org")
