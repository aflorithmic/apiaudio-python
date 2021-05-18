import aflr
import requests
import shutil
import os
import requests
from requests.exceptions import HTTPError


class APIRequest:
    def __init__(self, api_key=None, api_base=None, **params):
        self.api_key = api_key or aflr.api_key
        self.api_base = api_base or aflr.api_base
        if self.api_key == None or self.api_key == "your-key":
            self.api_key = os.environ.get("aflr_key", None)
        if self.api_key == None or len(self.api_key) < 30:
            raise ValueError(
                "Please specify a valid api_key or create one here:\nhttps://console.api.audio"
            )
        if not isinstance(self.api_key, str):
            raise TypeError("api_key must be of type string.")

    @classmethod
    def _build_header(self):
        # add more headers for analytics in the future
        return {"x-api-key": aflr.api_key}

    @classmethod
    def _post_request(cls, json, url=None):
        url = url or cls.url
        headers = cls._build_header()
        r = requests.post(url=url, headers=headers, json=json)
        cls._expanded_raise_for_status(r)
        return r.json()

    @classmethod
    def _get_request(cls, url=None, path_param=None, request_params=None):
        url = url or cls.url
        headers = cls._build_header()  # DRY. To be changed.
        if request_params:
            r = requests.get(url=url, headers=headers, params=request_params)
        elif path_param:
            r = requests.get(url=f"{url}/{path_param}", headers=headers)
        else:
            r = requests.get(url=url, headers=headers)
        cls._expanded_raise_for_status(r)
        return r.json()

    def _download_request(self, url, destination):
        local_filename = f"{destination}/{url.split('/')[-1].split('?')[0]}"
        local_filename = local_filename.replace("%243ct10n", "section")
        with requests.get(url, stream=True) as r:
            self._expanded_raise_for_status(r)
            with open(local_filename, "wb") as f:
                shutil.copyfileobj(r.raw, f)
        return local_filename

    @classmethod
    def config_test(cls):
        return f"Configured to transact {cls.OBJECT_NAME} objects to {cls.url} with api_key = {aflr.api_key}"

    @classmethod
    def _expanded_raise_for_status(self, res):
        """
        Take a "requests" response object and expand the raise_for_status method to return errors from API
        @param res:
        @return: None
        """
        try:
            res.raise_for_status()
        except HTTPError as e:
            if res.json():
                raise HTTPError(
                    "{} \n Error Message from API: \n {}".format(str(e), res.json())
                )
            else:
                raise e
        return
