from .api_request import APIRequest


class ListableResource(APIRequest):
    def __init__(self):
        super().__init__()

    @classmethod
    def list(cls, **args):
        if args:
            return cls._get_request(request_params=args)
        else:
            return cls._get_request()


class CreatableResource(APIRequest):
    def __init__(self):
        super().__init__()

    @classmethod
    def create(cls, **params):
        return cls._post_request(json=params)


class RetrievableResource(APIRequest):
    def __init__(self):
        super().__init__()

    @classmethod
    def retrieve(cls, scriptId, section=None, parameters=None):
        params = parameters or {}
        params.update({"scriptId": scriptId})

        if section:
            params.update({"section": section})

        if hasattr(cls, "file_url"):
            return cls._get_request(path_param=cls.file_url, request_params=params)
        else:
            return cls._get_request(request_params=params)


class DownloadableResource(APIRequest):
    def __init__(self):
        super().__init__()

    @classmethod
    def download(cls, scriptId, section=None, parameters=None, destination="."):
        parameters = parameters or {}

        try:
            audio_files = cls.retrieve(scriptId, section, parameters)
            audio_files.keys()
        except Exception:
            raise TypeError(
                "Error retriving the audiofiles. The response object is not a dict"
            )

        if "url" in audio_files.keys():
            local_filename = cls._download_request(
                url=audio_files.get("url"), destination=destination
            )
            return local_filename
        local_filenames = []
        for key, value in audio_files.items():
            # Review "value"! list of string...
            local_filename = cls._download_request(url=value, destination=destination)
            local_filenames.append(local_filename)

        return local_filenames
