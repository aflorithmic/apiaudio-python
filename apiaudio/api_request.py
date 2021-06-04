import apiaudio
import requests
import shutil
import os
import requests
from requests.exceptions import HTTPError


class APIRequest:
    def _api_key_checker(api_key=None):
        PLACEHOLDERS = ["your-key", "APIKEY", "API_KEY"]
        if api_key == None or api_key in PLACEHOLDERS:
            # aflr_key is for backward compatibility with the old name of env vars.
            api_key = os.environ.get("apiaudio_key", os.environ.get("aflr_key", None))
        if not isinstance(api_key, str):
            raise TypeError("api_key must be of type string.")

        if len(api_key) < 32:
            raise ValueError(
                "Please specify a valid api_key or create one here:\n https://console.api.audio"
            )
        apiaudio.api_key = api_key
        return

    @classmethod
    def _build_header(cls):
        cls._api_key_checker(apiaudio.api_key)
        return {"x-api-key": apiaudio.api_key}

    @classmethod
    def _post_request(cls, json, url=None):
        url = url or f"{apiaudio.api_base}{cls.resource_path}"

        headers = cls._build_header()
        r = requests.post(url=url, headers=headers, json=json)

        cls._expanded_raise_for_status(r)

        return r.json()

    @classmethod
    def _put_request_fileupload(cls, data, url=None, headers=None):
        url = url or f"{aflr.api_base}{cls.resource_path}"
        r = requests.put(url=url, headers=headers, data=data)
        cls._expanded_raise_for_status(r)
        return r

    @classmethod
    def _get_request(cls, url=None, path_param=None, request_params=None):
        url = url or f"{apiaudio.api_base}{cls.resource_path}"

        headers = cls._build_header()

        if path_param:
            url = f"{apiaudio.api_base}{path_param}"

        if request_params:
            r = requests.get(url=url, headers=headers, params=request_params)
        else:
            r = requests.get(url=url, headers=headers)

        cls._expanded_raise_for_status(r)

        return r.json()

    @classmethod
    def _download_request(cls, url, destination):
        local_filename = f"{destination}/{url.split('/')[-1].split('?')[0]}"
        local_filename = local_filename.replace("%243ct10n", "section")

        with requests.get(url, stream=True) as r:
            cls._expanded_raise_for_status(r)

            with open(local_filename, "wb") as f:
                shutil.copyfileobj(r.raw, f)

        return local_filename

    @classmethod
    def config_test(cls):
        return f"Configured to transact {cls.OBJECT_NAME} objects to {apiaudio.api_base}{cls.resource_path} with api_key = {apiaudio.api_key}"

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
                    "{} \n Error Message from API: \n {}".format(res.json(), str(e))
                )
            else:
                raise e
        return