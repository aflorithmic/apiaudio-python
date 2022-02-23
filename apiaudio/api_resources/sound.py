from apiaudio.helper_classes import (
    CreatableResource,
    ListableResource,
    RetrievableResource,
    DeletableResource
)

# These 3 classes are hidden from the user and are not included directly
#--
class SoundTemplate(
    CreatableResource, RetrievableResource, ListableResource, DeletableResource
):
    OBJECT_NAME = "soundTemplate"
    resource_path = "/sound/template"
    
class SoundSegment(
    CreatableResource, DeletableResource
):
    OBJECT_NAME = "soundSegment"
    resource_path = "/sound/segment"

class SoundParameter(
    ListableResource
):
    OBJECT_NAME = "soundParameter"
    resource_path = "/sound/parameter"


# --


# this class is included and wraps the above classes
class Sound():
    OBJECT_NAME = "sound"
    
    @classmethod
    def list_parameters(cls):
        return SoundParameter.list()

    @classmethod
    def list(cls, **args):
        return SoundTemplate().list(**args)

    @classmethod
    def create(cls, **params):
        return SoundTemplate.create(**params)

    @classmethod
    def delete(cls, **params):
        return SoundTemplate.delete(**params)
    
    @classmethod
    def add_segment(cls, **params):
        return SoundSegment.create(**params)
    
    
