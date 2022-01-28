from apiaudio.helper_classes import CreatableResource
from apiaudio.logging import SDKLogger


class Birdcache(CreatableResource):
    OBJECT_NAME = "birdcache"
    resource_path = "/birdcache"
    logger = SDKLogger(OBJECT_NAME)
