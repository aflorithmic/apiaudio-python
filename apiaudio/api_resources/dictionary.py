from apiaudio.helper_classes import ListableResource, RetrievableResource


class Lexi(ListableResource):
    OBJECT_NAME = "diction"
    resource_path = "/diction"

    list_words_path = resource_path + "/list/"
    list_types_path = resource_path + "/list_types"
    search_for_word_path = resource_path + "/search/"

    @classmethod
    def list_types(cls):
        return cls._get_request(path_param=cls.list_types_path)

    @classmethod
    def list_words(cls, dictId):
        return cls._get_request(path_param=cls.list_words_path + dictId)

    @classmethod
    def search_for_word(cls, word, lang):
        return cls._get_request(path_param=cls.search_for_word_path + f"{word}/{lang}")
