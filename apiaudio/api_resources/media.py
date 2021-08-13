from apiaudio.helper_classes import UploadableResource


class Media(UploadableResource):
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
    def list(cls, tags=None, mediaId= None):
        if mediaId:
            return cls._get_request(
                path_param=cls.audio_resource_path,
                request_params={"mediaId": mediaId},
            )
        if tags:
            return cls._get_request(
                path_param=cls.audio_resource_path,
                request_params={"tags": tags},
            )
        return cls._get_request(path_param=cls.audio_resource_path)

    @classmethod
    def list_tags(cls):
        return cls._get_request(path_param=f"{cls.audio_resource_path}/tags")
        