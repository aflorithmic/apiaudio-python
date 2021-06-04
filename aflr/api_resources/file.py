from posixpath import basename
import aflr
from aflr.helper_classes import APIRequest
import os


class File(APIRequest):
    custom_audio_resource_path = "/file/customaudio/"
    OBJECT_NAME = "file"
    resource_path = "/file"

    @classmethod
    def upload_audiofile(cls, file_path):
        # get presigned URL
        payload = open(file_path, "rb")
        filename = os.path.basename(file_path)
        headers = {"Content-Type": "audio/mpeg"}
        url = cls._get_request(
            path_param=cls.custom_audio_resource_path + "uploadurl?filename=" + filename
        )

        mediaId = url["mediaId"]
        fileUploadUrl = url["fileUploadUrl"]

        response = cls._put_request_fileupload(
            url=fileUploadUrl, headers=headers, data=payload
        )

        response = {
            "message": f"Success. Please make sure to save this mediaId : {mediaId}"
        }
        return response

    @classmethod
    def get_download_url(cls, metaId):
        return cls._get_request(
            path_param=cls.custom_audio_resource_path + "mediaid?mediaId=" + metaId
        )

    @classmethod
    def search_audiofiles(cls, tags=None):
        if tags:
            return cls._get_request(
                path_param=cls.custom_audio_resource_path + "tags?tags=" + tags
            )
        return cls._get_request(path_param=cls.custom_audio_resource_path + "org")
