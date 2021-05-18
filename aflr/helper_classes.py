from .api_request import APIRequest


class ListableResource(APIRequest):
    def __init__(self):
        super().__init__()

    @classmethod
    def list(cls):
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
    def retrieve(cls, objectId):
        return cls._get_request(path_param=objectId)
