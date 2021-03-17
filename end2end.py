import aflr
import requests
import time

aflr.api_key = "7pLmUFRgzEYa6Uvbs7qA11wH6hnoxfr856jdoWC8"


script = aflr.Script().create(
    scriptName="demo2",
    scriptText="<<sectionName::hello>> Hello from the sdk",
)

print(script)

response = aflr.Speech().create(
    scriptId=script.get("scriptId"),
)

print(response)
tts = aflr.Speech().retrieve(scriptId=script.get("scriptId"))

print(tts)


req_mastering = aflr.Mastering().request(
    scriptId=script.get("scriptId"),
    backgroundTrackId="full__citynights.wav",
)
print(req_mastering)

mastered_file = aflr.Mastering().retrieve(scriptId=script.get("scriptId"))
print(mastered_file)


sound = aflr.Sound().retrieve(
    scriptId=script.get("scriptId"),
    backgroundTrackId="full__citynights.wav",
)

print(sound)