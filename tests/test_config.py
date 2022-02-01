import apiaudio
import pprint
import pytest
import os 

apiaudio.api_key = os.environ["AFLR_API_KEY"]
#apiaudio.api_base="https://staging-v1.api.audio"

def test_list_parameters():
    assert len(apiaudio.Voice.list_parameters()) > 0 

def test_sound_design():
    sounds = apiaudio.Sound.list()
    print(sounds)

def test_create_scripts():
    create_script= apiaudio.Script.create(scriptId="test_sdk", scriptText="<<sectionName::question>> Hey! Do you know we support multiple voices from different providers in the same script? I am a polly voice from Amazon. <<sectionName::answer>> I am Azure voice from Microsoft. I think Azure voices sound awesome.")
    get_script = apiaudio.Script.retrieve(scriptId="test_sdk")
    apiaudio.Speech.create(scriptId="test_sdk", voice="brandon")

def test_create_mastering():
    create_script= apiaudio.Script.create(scriptText="<<sectionName::question>> Hey! Do you know we support multiple voices from different providers in the same script? I am a polly voice from Amazon. <<sectionName::answer>> I am Azure voice from Microsoft. I think Azure voices sound awesome.")
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
        scriptId="test_sdk",
        scriptText="...",
        versions=test_versions
    )
    
    assert script.get("availableVersions") == ["v0"] + [str(x) for x in test_versions.keys()]

    for ver in test_versions:
        speech = apiaudio.Speech.create(scriptId=script.get("scriptId"), version=ver)
        key = str(ver) + "|default"
        assert key in speech.keys()
        assert speech[key]["status_code"] == "201"
