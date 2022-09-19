import apiaudio
import pprint
import pytest
import os
import logging
from time import time

apiaudio.api_key = os.environ["AFLR_API_KEY"]
# apiaudio.api_base = "https://staging-v1.api.audio"


def test_level_setting():
    assert apiaudio._logger.level is logging.WARNING
    apiaudio.set_logger_level("DEBUG")
    assert apiaudio._logger.level is logging.DEBUG


def test_list_parameters():
    assert len(apiaudio.Voice.list_parameters()) > 0


def test_sound_design():
    sounds = apiaudio.Sound.list()
    print(sounds)


def test_create_scripts():
    create_script = apiaudio.Script.create(
        scriptId="test_sdk",
        scriptText="<<sectionName::question>> Hey! Do you know we support multiple voices from different providers in the same script? I am a polly voice from Amazon. <<sectionName::answer>> I am Azure voice from Microsoft. I think Azure voices sound awesome.",
    )
    get_script = apiaudio.Script.retrieve(scriptId="test_sdk")
    apiaudio.Speech.create(scriptId="test_sdk", voice="brandon")


def test_create_mastering():
    create_script = apiaudio.Script.create(
        scriptText="<<sectionName::question>> Hey! Do you know we support multiple voices from different providers in the same script? I am a polly voice from Amazon. <<sectionName::answer>> I am Azure voice from Microsoft. I think Azure voices sound awesome."
    )
    scriptId = create_script.get("scriptId")
    apiaudio.Speech.create(scriptId=scriptId, voice="brandon")
    mastering = apiaudio.Mastering.create(scriptId=scriptId)
    assert len(mastering) > 0
    assert len(mastering["url"]) > 0


def test_birdcache():
    birdcache = apiaudio.Birdcache.create(
        type="mastering",
        voice="linda",
        text="This is {{username|me}} creating synchronous text to speech",
        audience={"username": ["salih", "sam", "timo"]},
        soundTemplate="openup",
    )
    assert len(birdcache) > 0
    assert birdcache[1]["text"] == "This is salih creating synchronous text to speech"


def test_script_versions():
    from .assets import test_versions

    script = apiaudio.Script.create(
        scriptId="test_sdk", scriptText="hello...", versions=test_versions
    )

    assert script.get("availableVersions") == ["v0"] + [
        str(x) for x in test_versions.keys()
    ]

    for ver in test_versions:
        speech = apiaudio.Speech.create(scriptId=script.get("scriptId"), version=ver)
        key = str(ver) + "|default"
        assert key in speech.keys()
        assert speech[key]["status_code"] == "201"


def test_synctts():
    audio = apiaudio.SyncTTS.create(text="Hello, test 123!", voice="joanna")
    assert isinstance(audio, bytes)
    assert b"RIFF" in audio

    d = apiaudio.SyncTTS.create(text="Hello, test 123.", voice="joanna", url=True)
    assert isinstance(d, dict)
    assert "api.audio" in d.get("url", [])

    mp3_audio = apiaudio.SyncTTS.create(
        text="Hello, test 123.", voice="joanna", format="mp3"
    )
    assert isinstance(mp3_audio, bytes)
    assert not b"RIFF" in mp3_audio


def test_processing_loop_speech():
    t0 = time()
    speech = apiaudio.Speech.create(scriptId="longProcessing", voice="Dieter")
    assert len(speech) == 3  # number of sections in the script
    assert time() - t0 > 30


def test_processing_loop_mastering():
    t0 = time()
    apiaudio.Script.create(
        scriptId="test_sdk",
        scriptText="<<sectionName::question>> Hey! Do you know we support multiple voices from different providers in the same script? I am a polly voice from Amazon. <<sectionName::answer>> I am Azure voice from Microsoft. I think Azure voices sound awesome.",
    )
    apiaudio.Speech.create(scriptId="test_sdk", voice="brandon")
    mastering = apiaudio.Mastering.create(scriptId="test_sdk", forceLength=700)
    print(mastering)
    assert "url" in mastering
    assert time() - t0 > 30
