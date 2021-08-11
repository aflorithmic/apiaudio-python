from apiaudio.helper_classes import (
    CreatableResource,
    ListableResource,
    RetrievableResource,
)


class Script(ListableResource, CreatableResource, RetrievableResource):
    OBJECT_NAME = "script"
    resource_path = "/script"
    random_url = "/script/random"

    @classmethod
    def get_random_text(cls, category=None):
        return cls._get_request(
            path_param=cls.random_url, request_params={"category": category}
        )
