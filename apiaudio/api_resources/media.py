from apiaudio.helper_classes import UploadableResource


class Media(UploadableResource):
    OBJECT_NAME = "media"
    resource_path = "/file"
    audio_resource_path = "/file/customaudio"

    @classmethod
    def get_download_url(cls, mediaId: str = ""):
        if not mediaId:
            raise ValueError("please specify a mediaId")

        url = (
            cls.list(mediaId=mediaId, downloadUrl=True)
            .get("savedAudioFiles", [{}])[0]
            .get("downloadUrl", None)
        )

        if not url:
            raise ValueError("url could not be retrieved")

        return url

    @classmethod
    def list(cls, tags: str = "", mediaId: str = "", downloadUrl: bool = False) -> dict:
        request_params = {}

        if downloadUrl:
            request_params["target"] = "download"

        if mediaId:
            return cls._get_request(
                path_param=cls.audio_resource_path,
                request_params={**request_params, **{"mediaId": mediaId}},
            )
        if tags:
            return cls._get_request(
                path_param=cls.audio_resource_path,
                request_params={**request_params, **{"tags": tags}},
            )
        return cls._get_request(
            path_param=cls.audio_resource_path, request_params=request_params
        )

    @classmethod
    def list_tags(cls):
        return cls._get_request(path_param=f"{cls.audio_resource_path}/tags")

    @classmethod
    def download(cls, mediaId: str = "", destination: str = "."):
        url = cls.get_download_url(mediaId=mediaId)

        return cls._download_request(url=url, destination=destination)
