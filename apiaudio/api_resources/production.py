# class Speech(CreatableResource, RetrievableResource, DownloadableResource, ListableResource):
#     OBJECT_NAME = "speech"
#     resource_path = "/speech"
#     loop_status_code = 202


#     @classmethod
#     def get(cls, speechId):
#         return cls._get_request(path_param=cls.resource_path + "/" + speechId)
#         #return cls.get download(cls, CreateThreeSections.create(**args))
    
    
    
    
#     @classmethod
#     def download(cls, speechId, destination="."):
#         r = cls.get(speechId=speechId)
#         files = []
#         if r:
#             for section in r["sections"]:
#                 url = section["url"]
#                 sectionName = section["sectionName"]
#                 r = requests.get(url, stream=True)
#                 local_filename = f"{destination}/{sectionName}.wav"
#                 files.append(sectionName)   
#                 with open(local_filename, "wb") as f:
#                     shutil.copyfileobj(r.raw, f)
#                 local_filename = cls._download_request(
#                     url=url, destination=destination
#                 )
                
            
#         return "Downloaded : " ', '.join(files)

from apiaudio.helper_classes import (
    ListableResource,
    CreatableResource,
    DownloadableResource,
    RetrievableResource,
)

import requests
import shutil

class Production(CreatableResource, RetrievableResource, DownloadableResource, ListableResource):
    OBJECT_NAME = "productionId"
    resource_path = "/production"
    mastering_preset_list_path = resource_path + "-presets"

    loop_status_code = 202

    @classmethod
    def list_presets(cls):
        return cls._get_request(path_param=cls.mastering_preset_list_path)
    @classmethod
    def get(cls, productionId):
        return cls._get_request(path_param=cls.resource_path + "/" + productionId)
        
    
    @classmethod
    def download(cls, productionId, destination=".", name="default"):
        r = cls.get(productionId=productionId)
        print(r)
        files = []

        # if 'url' in r:
        #     url = r['url']
        #     r = requests.get(url, stream=True)
        #     local_filename = f"{destination}/{name}.wav"
        #     files.append(name)   
        #     with open(local_filename, "wb") as f:
        #         shutil.copyfileobj(r.raw, f)
        #     local_filename = cls._download_request(
        #         url=url, destination=destination
        #     )
        
        if r:
            for i, section in enumerate(r["files"]):
                url = section["url"]
                sectionName = name + f"_{i}"
                r = requests.get(url, stream=True)
                local_filename = f"{destination}/{sectionName}.wav"
                files.append(sectionName)   
                with open(local_filename, "wb") as f:
                    shutil.copyfileobj(r.raw, f)
                local_filename = cls._download_request(
                    url=url, destination=destination
                )
        res = "Downloaded : " + ', '.join(files)
        return res