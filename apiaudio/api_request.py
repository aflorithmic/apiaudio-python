import apiaudio
import requests
import shutil
import os
import requests
import re

from requests.exceptions import HTTPError
from . import sdk_version
from apiaudio.logging import SDKLogger


class APIRequest:
    def _api_key_checker(api_key=None):
        api_key_error_message = "Please specify a valid api_key or create one here:\n https://console.api.audio"
        PLACEHOLDERS = ["your-key", "APIKEY", "API_KEY"]
        if api_key == None or api_key in PLACEHOLDERS:
            # aflr_key is for backward compatibility with the old name of env vars.
            api_key = os.environ.get("apiaudio_key", os.environ.get("aflr_key"))

            if api_key == None:
                raise TypeError(f"No api_key has been found. {api_key_error_message}")

        if not isinstance(api_key, str):
            raise TypeError("api_key must be of type string.")

        if len(api_key) < 32:
            raise ValueError(
                f"api_key has less than 32 characters. {api_key_error_message}"
            )
        apiaudio.api_key = api_key
        return

    @classmethod
    def _build_header(cls):
        cls._api_key_checker(apiaudio.api_key)
        return {"x-api-key": apiaudio.api_key, "x-python-sdk-version": sdk_version}

    @classmethod
    def _post_request(cls, json, url=None):
        url = url or f"{apiaudio.api_base}{cls.resource_path}"
        headers = cls._build_header()
        r = requests.post(url=url, headers=headers, json=json)

        # speech timeouts
        if r.status_code == 504:
            r = requests.get(url=url, headers=headers, params=json)

        cls._expanded_raise_for_status(r)

        return r.json()

    @classmethod
    def _post_request_raw(cls, json, url=None, istype="wav"):
        url = url or cls.resource_path
        url = f"{apiaudio.api_base}{url}"
        headers = cls._build_header()
        if istype == "wav":
            headers["Accept"] = "audio/wav"
        r = requests.post(url=url, headers=headers, json=json)

        cls._expanded_raise_for_status(r)

        return r.content

    @classmethod
    def _delete_request(cls, url=None, path_param=None, request_params=None):
        url = url or f"{apiaudio.api_base}{cls.resource_path}"

        headers = cls._build_header()
        if path_param:
            url = f"{apiaudio.api_base}{path_param}"

        if request_params:
            r = requests.delete(url=url, headers=headers, params=request_params)
        else:
            r = requests.delete(url=url, headers=headers)

        cls._expanded_raise_for_status(r)

        return r.json()

    @classmethod
    def _put_request(cls, data, url=None, headers=None):
        url = url or f"{apiaudio.api_base}{cls.resource_path}"

        r = requests.put(url=url, headers=headers, data=data)

        cls._expanded_raise_for_status(r)

        if r.status_code != 200:
            raise ValueError("Error performing the PUT request")

        # since aws s3 does not return a body on PUT requests,
        # r.json() does not work here
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
    def _download_request(cls, url, destination, version=""):
        if type(url) is not str:
            raise TypeError("Error retrieving the audio files.")

        remote_filename = url.split("/")[-1].split("?")[0]
        local_filename = f"{destination}/{remote_filename}"
        local_filename = local_filename.replace("%243ct10n", "section")
        local_filename = local_filename.replace("%7C", "|")

        response = requests.get(url, stream=True)
        while response.status_code == 202:  # keep the retrieval going if 202 returned
            response = requests.get(url, stream=True)

        cls._expanded_raise_for_status(response)

        with open(local_filename, "wb") as f:
            shutil.copyfileobj(response.raw, f)

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
            if apiaudio.log_warnings:
                latest_version = res.headers.get("x-sdk-latest", apiaudio.sdk_version)
                if (
                    latest_version != apiaudio.sdk_version
                    and not apiaudio._version_warning_issued
                ):
                    apiaudio._logger.warning(
                        f"The latest version of apiaudio is {latest_version} and the version you're using is {apiaudio.sdk_version}. Consider upgrading, as you might be missing out on new features and bug fixes."
                    )
                    apiaudio._version_warning_issued = True

                if res.headers.get("Warning") and apiaudio.log_warnings:
                    for warn in re.findall(
                        r"\"(.*?)\"", res.headers["Warning"]
                    ):  # get all messages in between ""
                        apiaudio._logger.warning(f"{self.OBJECT_NAME.upper()}: {warn}")

            res.raise_for_status()
        except HTTPError as e:
            if res.json():
                raise HTTPError(
                    "{} \n Error Message from API: \n {}".format(res.json(), str(e))
                )
            else:
                raise e
        return
