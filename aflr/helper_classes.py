from .api_request import APIRequest


class listableResource(APIRequest):
    def __init__(self):
        super().__init__()

    @classmethod
    def list(cls):
        return cls._get_request()
