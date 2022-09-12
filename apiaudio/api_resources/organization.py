from apiaudio.api_request import APIRequest


class Organization(APIRequest):
    OBJECT_NAME = "organization"
    resource_path = "/org"
    child_orgs_path = "/org/child_orgs"
    secrets_path = "/secrets"

    @classmethod
    def get_secrets(cls):
        return cls._get_request(path_param=cls.secrets_path)

    @classmethod
    def get_org_data(cls):
        return cls._get_request()

    @classmethod
    def list_child_orgs(cls):
        return cls._get_request(path_param=cls.child_orgs_path)
