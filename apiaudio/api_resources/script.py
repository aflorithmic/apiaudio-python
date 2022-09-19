from apiaudio.helper_classes import (
    CreatableResource,
    DeletableResource,
    ListableResource,
    RetrievableResource,
)


class Project(ListableResource):
    OBJECT_NAME = "script/list_projects"
    resource_path = "/script/list_projects"

class Module(ListableResource):
    OBJECT_NAME = "script/list_modules"
    resource_path = "/script/list_modules"

class ScriptName(ListableResource):
    OBJECT_NAME = "script/list_script_names"
    resource_path = "/script/list_script_names"

class Script(
    ListableResource, CreatableResource, RetrievableResource, DeletableResource
):
    OBJECT_NAME = "script"
    resource_path = "/script"
    random_url = "/script/random"

    class Directory():
        @classmethod 
        def list_projects(cls, **args):
            return Project.list(**args)

        @classmethod 
        def list_modules(cls, **args):
            return Module.list(**args)
        
        @classmethod 
        def list_script_names(cls, **args):
            return ScriptName.list(**args)
    
    @classmethod
    def get_random_text(cls, category=None):
        return cls._get_request(
            path_param=cls.random_url, request_params={"category": category}
        )

    @classmethod
    def preview(cls, scriptId, voice):
        params = {"preview": True, "voice": voice}
        r = cls._get_request(
            path_param=cls.resource_path + f"/{scriptId}", request_params=params
        )

        if "scriptText" in r:
            res = {"preview": r["scriptText"]}
            if "wordsNotInDict" in r:
                res["wordsNotInDict"] = r["wordsNotInDict"]

            return res
        else:  # in practice this won't happen as _get_request raises an exception
            return "PREVIEW FAILED"

    @classmethod
    def delete_multiple(cls, projectName, moduleName="", scriptName=""):
        
        params = {
            "projectName" : projectName,
            "moduleName" : moduleName,
            "scriptName" : scriptName
        }
        params = dict( [(k,v) for k,v in params.items() if v])

        
        return cls._delete_request(
            path_param=cls.resource_path + "s",
            request_params=params
            )