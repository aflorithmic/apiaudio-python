from aflr.helper_classes import CreatableResource, ListableResource, RetrievableResource


class Script(ListableResource, CreatableResource, RetrievableResource):
    OBJECT_NAME = "script"
    resource_path = "/script"
    random_url = "/script/random"

    @classmethod
    def create_random(cls, randomText=None):
        return cls._get_request(
            path_param=cls.random_url, request_params={"randomText": randomText}
        )

