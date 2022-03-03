from ast import arg
from apiaudio.helper_classes import (
    CreatableResource,
    DownloadableResource,
    RetrievableResource,
)

class CreateMediaWithSound(CreatableResource):
    OBJECT_NAME = "orchestrator"
    resource_path = "/orchestrator/media_with_sound"

class CreateAudio(CreatableResource):
    OBJECT_NAME = "orchestrator"
    resource_path = "/orchestrator/create_audio"

class CreateThreeSections(CreatableResource):
    OBJECT_NAME = "orchestrator"
    resource_path = "/orchestrator/create_three_sections"


class Orchestrator(CreatableResource):
    OBJECT_NAME = "orchestrator"
    resource_path = "/orchestrator"

    # just wrappers for the above classes
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
        local_filename = cls._download_request(
            url=response.get("url"), destination="."
        )
        return local_filename




    #         @classmethod
    # def create_audio(cls, scriptText, voice, soundTemplate):
    #     #return cls._get_request(path_param=cls.search_for_word_path + f"{word}/{lang}")
    #     body = {"scriptText" : scriptText, "voice" : voice, "soundTemplate" : soundTemplate}
    #     response = cls._post_request(json=body, url="https://staging-v1.api.audio/orchestrator/create_audio")

    #     local_filename = cls._download_request(
    #         url=response.get("url"), destination="."
    #     )
    #     return local_filename

