from apiaudio.helper_classes import CreatableResource, ListableResource, RetrievableResource


class LexiItem(CreatableResource, RetrievableResource):
    OBJECT_NAME = "diction/custom/item"
    resource_path = "/diction/custom/item"
    

class Lexi(ListableResource):
    OBJECT_NAME = "diction"
    resource_path = "/diction"

    custom_word_path = resource_path + "/custom/item"
    list_words = resource_path + "/custom"
    

    @classmethod
    def register_word(cls, **params):
        return cls._put_request(data=params, url=obj)

    @classmethod
    def list_words(cls, dictId):
        return cls._get_request(path_param=cls.list_words_path + dictId)

    @classmethod
    def search_for_word(cls, word, lang):
        return cls._get_request(path_param=cls.search_for_word_path + f"{word}/{lang}")
