
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
    assert len(Voice().list(language="spanish").get("voices")) == 7

def test_list_parameters():
    assert len(Voice().list_parameters()) > 0 

def test_sound_design():
    sounds = Sound().list_sound_templates()
    city_nights=sounds.get("templateFiles").get("citynights")
    assert city_nights[1].keys() == dict_keys(['citynights__music.wav'])