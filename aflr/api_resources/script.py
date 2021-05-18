from aflr.helper_classes import CreatableResource, ListableResource, RetrievableResource
import aflr


class Script(ListableResource, CreatableResource, RetrievableResource):
    OBJECT_NAME = "script"
    url = f"{aflr.api_base}/{OBJECT_NAME}"