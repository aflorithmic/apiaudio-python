from apiaudio.helper_classes import (
    CreatableResource,
    DeletableResource,
    ListableResource,
    RetrievableResource,
)


class Script(ListableResource, CreatableResource, RetrievableResource, DeletableResource):
    OBJECT_NAME = "script"
    resource_path = "/script"
    random_url = "/script/random"

    @classmethod
    def create(cls, **params):
        if 'scriptId' in params:
            try:
                response = Script.retrieve(scriptId=params['scriptId'])
                print("Warning - This scriptId already exists. You should use update(). This will be deprecated in future versions of the API")
                # -> re-direct to update
                return super(Script, cls).create(**params)

            except Exception as e:
                return super(Script, cls).create(**params)
        
        #return cls._post_request(json=params)

    @classmethod
    def get_random_text(cls, category=None):
        return cls._get_request(
            path_param=cls.random_url, request_params={"category": category}
        )
