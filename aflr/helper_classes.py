from .api_request import APIRequest


class ListableResource(APIRequest):
    def __init__(self):
        super().__init__()

    @classmethod
    def list(cls):
        return cls._get_request()
