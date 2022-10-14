import requests
import shutil
from apiaudio.helper_classes import (
    CreatableResource,
    DownloadableResource,
    ListableResource,
    RetrievableResource,
)


class Speech(CreatableResource, RetrievableResource, DownloadableResource, ListableResource):
    OBJECT_NAME = "speech"
    resource_path = "/speech"
    loop_status_code = 202


    @classmethod
    def get(cls, speechId):
        return cls._get_request(path_param=cls.resource_path + "/" + speechId)
        #return cls.get download(cls, CreateThreeSections.create(**args))
    
    
    
    
    @classmethod
    def download(cls, speechId, destination="."):
        r = cls.get(speechId=speechId)
        files = []
        if r:
            for section in r["sections"]:
                url = section["url"]
                sectionName = section["sectionName"]
                r = requests.get(url, stream=True)
                local_filename = f"{destination}/{sectionName}.wav"
                files.append(sectionName)   
                with open(local_filename, "wb") as f:
                    shutil.copyfileobj(r.raw, f)
                local_filename = cls._download_request(
                    url=url, destination=destination
                )
                
            
        return "Downloaded : " ', '.join(files)