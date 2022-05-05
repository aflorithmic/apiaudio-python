from apiaudio.helper_classes import CreatableResource, HelpResource


class CreateMediaWithSound(CreatableResource):
    OBJECT_NAME = "orchestrator"
    resource_path = "/orchestrator/media_with_sound"


class CreateAudio(CreatableResource):
    OBJECT_NAME = "orchestrator"
    resource_path = "/orchestrator/create_audio"


class CreateThreeSections(CreatableResource):
    OBJECT_NAME = "orchestrator"
    resource_path = "/orchestrator/create_three_sections"


class Orchestrator(CreatableResource, HelpResource):
    OBJECT_NAME = "orchestrator"
    resource_path = "/orchestrator"

    @classmethod
    def create_media_with_sound(cls, **args):
        return cls.download(cls, CreateMediaWithSound.create(**args))

    @classmethod
    def create_audio(cls, **args):
        return cls.download(cls, CreateAudio.create(**args))

    @classmethod
    def create_three_sections(cls, **args):
        return cls.download(cls, CreateThreeSections.create(**args))

    def download(cls, response):
        local_filename = cls._download_request(url=response.get("url"), destination=".")
        return local_filename
