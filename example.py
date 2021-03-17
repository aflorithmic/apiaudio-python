import aflr

aflr.api_key = "vyCTlS1hLc5N5N1CON2nh2qtU6PBz7vY1MFfIlS6"
script_id = "9ce62509-4d80-43bb-92c4-cab722b253aa"
# Create a new script and print the script created
script = aflr.Script().create(
    scriptName="exoTest",
    scriptText="<<sectionName::hello>> Hello world! This is awesome!! <<sectionName::goodbye>> It even works when I say goodbye from Trier {{username|lars}}",
)
print(script)

# Retrieve the script item and print the script created
script = aflr.Script().retrieve(scriptId=script["scriptId"])
print(script)

# create a text-to-speech
response = aflr.Speech().create(
    scriptId=script_id, audience=[{"username": "larsPlaceholder"}]
)
print(response)

# # get the speech audio files
audio_files = aflr.Speech().retrieve(scriptId=script_id)
print(audio_files)

# download all speech audio files
# check your folder :) you should have the following audio_files
# audio_files = aflr.Speech().download(scriptId=script["scriptId"], destination=".")
# print(audio_files)

# Get all available voices and print the first one
# all_voices = aflr.Voice().list()
# print(all_voices["voices"][0])
