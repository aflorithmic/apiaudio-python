from apiaudio.api_request import APIRequest


class Connector(APIRequest):
    OBJECT_NAME = "connector"
    resource_path = "/connector/"
    connection_path = "/connection/"

    @classmethod
    def retrieve(cls, name):
        if not name:
            raise Exception("Name must be set")
        return cls._get_request(path_param=cls.resource_path + name)

    @classmethod
    def connection(cls, connection_id):
        if not connection_id:
            raise Exception("Connection id must be set")
        return cls._get_request(path_param=cls.connection_path + connection_id)
