import aflr

aflr.api_key = "your-key"

# Create a new script and print the script created
script = aflr.Script().create(scriptText="Hello world")
print(script)

# Retrieve the script item and print the script created
script = aflr.Script().retrieve(scriptId=script["scriptId"])
print(script)

# Retrieve all scripts and print the first's script text
scripts = aflr.Script().list()
print(scripts[0]["scriptText"])

# create a text-to-speech
response = aflr.Speech().create(scriptId=script["scriptId"])
print(response)

# get the speech audio files
audio_files = aflr.Speech().retrieve(scriptId=script["scriptId"])
print(audio_files)

# download all speech audio files
# check your folder :) you should have the following audio_files
audio_files = aflr.Speech().download(scriptId=script["scriptId"], destination=".")
print(audio_files)

# Get all available voices and print the first one
all_voices = aflr.Voice().list()
print(all_voices["voices"][0])
