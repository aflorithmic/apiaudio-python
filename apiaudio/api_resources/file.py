from aflr.helper_classes import UploadableResource, ListableResource


class File(UploadableResource, ListableResource):
    custom_audio_resource_path = "/file/customaudio/"
    OBJECT_NAME = "file"
    resource_path = "/file"

    @classmethod
    def get_download_url(cls, metaId):
        return cls._get_request(
            path_param=cls.custom_audio_resource_path + "mediaid?mediaId=" + metaId
        )

    @classmethod
    def list(cls, tags=None):
        if tags:
            return cls._get_request(
                path_param=cls.custom_audio_resource_path + "tags?tags=" + tags
            )
        return cls._get_request(path_param=cls.custom_audio_resource_path + "org")
