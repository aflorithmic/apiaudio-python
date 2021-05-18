from aflr.helper_classes import CreatableResource, ListableResource, RetrievableResource
import aflr


class Script(ListableResource, CreatableResource, RetrievableResource):
    OBJECT_NAME = "script"
    resource_path = "/script"
