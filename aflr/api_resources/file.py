from posixpath import basename
import aflr
from aflr.helper_classes import ListableResource
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import requests
import json


class File(ListableResource):
    OBJECT_NAME = "file"
    resource_path = "/file"
    custom_audio_upload = "/file/customaudio/uploadurl?filename="
    by_tag = "/file/customaudio/tags?tags="
    by_metaId = "/file/customaudio/mediaid?mediaId="
    by_org = "/file/customaudio/org"

    @classmethod
    def upload_audiofile(cls):
        # get presigned URL
        payload = askopenfilename()
        filename = os.path.basename(payload)
        headers = {"Content-Type": "audio/mpeg"}
        print("URL", cls.custom_audio_upload)
        url = cls._get_request(path_param=cls.custom_audio_upload + filename)

        mediaId = url["mediaId"]
        fileUploadUrl = url["fileUploadUrl"]
        print("mediaId", mediaId)

        # Do put request with presigned URL
        response = requests.request(
            "PUT", url=fileUploadUrl, headers=headers, data=payload
        )

        response = {
            "message": f" Success. Please make sure to save this mediaId : {mediaId}"
        }
        return response

    @classmethod
    def download_audiofile(cls, metaId):
        url = cls._get_request(path_param=cls.by_metaId + metaId)
        return url

    @classmethod
    def search_audiofiles(cls):
        response = cls._get_request(path_param=cls.by_org)
        return response

    @classmethod
    def search_audiofiles_by_tag(cls, tags):
        url = cls._get_request(path_param=cls.by_tag + tags)
        return url


# get speech files
# TBD

# get sound files
# TBD
