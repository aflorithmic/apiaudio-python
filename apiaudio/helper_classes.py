import os

from .api_request import APIRequest


class ListableResource(APIRequest):
    @classmethod
    def list(cls, **args):
        if args:
            return cls._get_request(request_params=args)
        else:
            return cls._get_request()


class HelpResource(APIRequest):
    @classmethod
    def help(cls, **params):
        return cls._options_request()


class CreatableResource(APIRequest):
    @classmethod
    def create(cls, **params):
        return cls._post_request(json=params)


class UpdatableResource(APIRequest):
    @classmethod
    def update(cls, **params):
        return cls._put_request(json=params)


class DeletableResource(APIRequest):
    @classmethod
    def delete(cls, **args):

        if cls.OBJECT_NAME == "media":
            if "mediaId" not in args:
                raise Exception("mediaId parameter is required")

            return cls._delete_request(
                path_param=cls.audio_resource_path, request_params=args
            )

        if cls.OBJECT_NAME == "script":
            if "scriptId" not in args:
                raise Exception("scriptId parameter is required")
            else:
                scriptId = args["scriptId"]
            if "version" in args:
                version = args["version"]
                return cls._delete_request(
                    path_param=f"{cls.resource_path}/{scriptId}/{version}"
                )
            else:
                return cls._delete_request(path_param=f"{cls.resource_path}/{scriptId}")

        return cls._delete_request(request_params=args)


class RetrievableResource(APIRequest):
    @classmethod
    def retrieve(
        cls,
        scriptId,
        version=None,
        section=None,
        parameters=None,
        public=None,
        vast=None,
        endFormat=None,
        requestId=None,
    ):
        params = parameters.copy() if parameters else {}
        params.update({"scriptId": scriptId})

        if section:
            params.update({"section": section})

        if public is not None:
            params.update({"public": public})

        if vast is not None:
            params.update({"vast": vast})

        if endFormat is not None:
            params.update({"endFormat": endFormat})

        if version is not None:
            params.update({"version": version})

        if requestId is not None:
            params.update({"requestId": requestId})

        if cls.OBJECT_NAME == "script":
            if version is not None:
                return cls._get_request(
                    path_param=f"{cls.resource_path}/{scriptId}", request_params=params
                )
            else:
                return cls._get_request(path_param=f"{cls.resource_path}/{scriptId}")

        if hasattr(cls, "file_url"):
            return cls._get_request(path_param=f"{cls.file_url}")
        else:
            return cls._get_request(request_params=params)


class DownloadableResource(APIRequest):
    @classmethod
    def download(
        cls,
        scriptId,
        version=None,
        section=None,
        parameters=None,
        public=None,
        vast=None,
        endFormat=None,
        destination=".",
    ):
        parameters = parameters or {}

        try:
            audio_files = cls.retrieve(
                scriptId, version, section, parameters, public, vast, endFormat
            )
            audio_files.keys()
        except Exception:
            raise TypeError(
                "Error retrieving the audio files. Make sure you can retrieve them with the same parameters and try again."
            )

        if "url" in audio_files.keys():
            local_filename = cls._download_request(
                url=audio_files.get("url"), destination=destination
            )
            return local_filename

        else:
            local_filenames = []
            for key, value in audio_files.items():
                # if key == "url": # placeholder for future versions
                local_filename = cls._download_request(
                    url=value, destination=destination
                )
                local_filenames.append(local_filename)

        return local_filenames


class UploadableResource(APIRequest):
    @classmethod
    def upload(cls, file_path: str = "", tags: str = ""):
        payload = open(file_path, "rb")
        filename = os.path.basename(file_path)
        headers = {"Content-Type": "audio/mpeg"}

        request_params = {"filename": filename}

        if tags:
            request_params["tags"] = tags

        # get presigned URL
        url = cls._get_request(
            path_param=f"{cls.audio_resource_path}/uploadurl",
            request_params=request_params,
        )

        mediaId = url["mediaId"]
        fileUploadUrl = url["fileUploadUrl"]

        response = cls._put_request_s3(url=fileUploadUrl, headers=headers, data=payload)

        payload.close()

        response = {
            "message": f"Success. Use mediaId to retrieve this file",
            "mediaId": mediaId,
        }

        return response
