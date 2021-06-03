
import aflr
from aflr import Script, Sound, Speech, Mastering, Voice
import pprint
import pytest
import os 

aflr.api_key = os.getenv("AFLR_API_KEY_PEADAR")
def test_english_voices():
    print("List test:\nAll voices:")
    print(len(Voice().list().get("voices")))
    print("\nFiltered voices:")
    assert len(Voice().list(language="english").get("voices")) == 16

def test_spanish_voices():
    assert len(Voice.list(language="spanish").get("voices")) == 7

def test_list_parameters():
    assert len(Voice.list_parameters()) > 0 

def test_sound_design():
    sounds = Sound.list_sound_templates()
    city_nights=sounds.get("templateFiles").get("citynights")
    # Still not sure how to get this to work properly
    assert len(city_nights) > 0
    assert list(city_nights[1]) == ['citynights__music.wav']

def test_create_scripts():
    create_script= Script.create(scriptText="<<sectionName::question>> Hey! Do you know we support multiple voices from different providers in the same script? I am a polly voice from Amazon. <<sectionName::answer>> I am Azure voice from Microsoft. I think Azure voices sound awesome.")
    scriptId = create_script.get("scriptId")
    create_speech = Speech.create(scriptId=scriptId)
    create_tts = {'message': 'Success. Text-to-speech is in progress.'}
    assert create_speech == create_tts

def test_create_mastering():
    create_script= Script().create(scriptText="<<sectionName::question>> Hey! Do you know we support multiple voices from different providers in the same script? I am a polly voice from Amazon. <<sectionName::answer>> I am Azure voice from Microsoft. I think Azure voices sound awesome.")
    scriptId = create_script.get("scriptId")
    Speech().create(scriptId=scriptId)
    mastering = Mastering.create(scriptId=scriptId)
    create_mastering = {'Message': 'Mastering request was successful'}
    assert len(mastering) > 0
    assert mastering == create_mastering
