from apiaudio.helper_classes import (
    CreatableResource,
    DeletableResource,
    ListableResource,
    RetrievableResource,
)


class Script(
    ListableResource, CreatableResource, RetrievableResource, DeletableResource
):
    OBJECT_NAME = "script"
    resource_path = "/script"
    random_url = "/script/random"
    api_redirect = ""

    @classmethod
    def get_random_text(cls, category=None):
        return cls._get_request(
            path_param=cls.random_url, request_params={"category": category}
        )

    @classmethod
    def preview(cls, scriptId, voice):
        params = {"preview": True, "voice": voice}
        r = cls._get_request(
            path_param=cls.resource_path + f"/{scriptId}", request_params=params
        )

        if "scriptText" in r:
            res = {"preview": r["scriptText"]}
            if "wordsNotInDict" in r:
                res["wordsNotInDict"] = r["wordsNotInDict"]

            return res
        else:  # in practice this won't happen as _get_request raises an exception
            return "PREVIEW FAILED"
