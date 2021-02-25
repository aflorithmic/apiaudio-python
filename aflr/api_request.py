import aflr
import requests
import shutil
import os


class APIRequest:
    def __init__(self, api_key=None, api_base=None, **params):
        self.api_key = api_key if api_key else aflr.api_key
        self.api_base = api_base if api_base else aflr.api_base
        if self.api_key == None or self.api_key == "your-key":
            self.api_key = os.environ.get("aflr_key", None)
        if self.api_key == None or len(self.api_key) < 30:
            raise ValueError("Please specify a valid api_key.")
        if not isinstance(self.api_key, str):
            raise TypeError("api_key must be of type string.")

    def _build_header(self):
        # add more headers for analytics in the future
        return {"x-api-key": self.api_key}

    def _post_request(self, json, url=None):
        url = self.url if not url else url
        headers = self._build_header()
        r = requests.post(url=url, headers=headers, json=json)
        return r.json()

    def _get_request(self, url, path_param=None, request_params=None):
        headers = self._build_header()  # DRY. To be changed.
        if request_params:
            r = requests.get(url=url, headers=headers, params=request_params)
        elif path_param:
            r = requests.get(url=f"{url}/{path_param}", headers=headers)
        else:
            r = requests.get(url=url, headers=headers)
        return r.json()

    def _download_request(self, url, destination):
        local_filename = f"{destination}/{url.split('/')[-1].split('?')[0]}"
        local_filename = local_filename.replace("%243ct10n", "section")
        with requests.get(url, stream=True) as r:
            with open(local_filename, "wb") as f:
                shutil.copyfileobj(r.raw, f)
        return local_filename
