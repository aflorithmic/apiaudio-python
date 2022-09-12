from apiaudio.helper_classes import (
    UpdatableResource,
    ListableResource,
    DeletableResource,
)


class LexiItem(UpdatableResource, ListableResource, DeletableResource):
    OBJECT_NAME = "diction/custom/item"
    resource_path = "/diction/custom/item"


class CustomDict(ListableResource):
    OBJECT_NAME = "diction/custom"
    resource_path = "/diction/custom"


class Lexi(ListableResource):
    OBJECT_NAME = "diction"
    resource_path = "/diction"

    custom_word_path = resource_path + "/custom/item"
    list_words = resource_path + "/custom"

    @classmethod
    def register_custom_word(
        cls, word, replacement, lang, specialization="default", contentType="basic"
    ):
        return LexiItem.update(
            **{
                "word": word,
                "replacement": replacement,
                "lang": lang,
                "specialization": specialization,
                "contentType": contentType,
            }
        )

    @classmethod
    def list_custom_words(cls, **args):
        return LexiItem.list(**args)

    @classmethod
    def list_custom_dicts(cls, **args):
        return CustomDict.list(**args)

    @classmethod
    def delete_custom_word(cls, **args):
        return LexiItem.delete(**args)
