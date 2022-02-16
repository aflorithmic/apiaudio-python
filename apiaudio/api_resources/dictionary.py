from apiaudio.helper_classes import (
    ListableResource,
    RetrievableResource
)


class Lexi(ListableResource):
    OBJECT_NAME = "diction"
    resource_path = "/diction"
    list_path = resource_path + "/get_dicts_all"
    get_dicts_path = resource_path + "/get_dicts"
    get_dict_path = resource_path + "/get_dict"
    search = resource_path + "/search"
    type = resource_path + "/get_type"
    api_redirect = ""


    @classmethod
    def list(cls, **args):
        return cls._get_request(path_param=cls.list_path, request_params=args)


    
    @classmethod
    def get_dicts_by_language(cls, language):
         return cls._get_request(path_param=cls.get_dicts_path + "/" + language)#, request_params={"lang":language})

    @classmethod
    def get_dict_by_id(cls, dictId):
        return cls._get_request(path_param=cls.get_dict_path + "/id/" + dictId)

    @classmethod
    def get_dict_by_type(cls, type, language):
        return cls._get_request(path_param=cls.type + f"/{type}/{language}")

    @classmethod
    def search_for_word(cls, word, language):
        return cls._get_request(path_param=cls.search + f"/{word}/{language}")

    # def retrieve(name):
    #     if name == "ukcities":
    #         return {"reading", "manchester", "liverpool", "cardiff", "edinburgh"}
    #     if name == "uknames":
    #         return {"sam", "anne", "timo", "peadar", "marcin"}
    #     return {}