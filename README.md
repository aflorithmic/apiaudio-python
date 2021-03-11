# aflr

aflr is the official api.audio Python SDK. This SDK provides easy access to the api.audio API from applications written in python.

## Documentation

For examples, recipes and api reference see the [api.audio docs](https://docs.api.audio/reference)

## Installation

You don't need this source code unless you want to modify it. If you want to use the package, just run:

```sh
pip install aflr -U
```

Install from source with:

```sh
python setup.py install
```

## Requirements

Python 3.6+

# Getting started

## Setup

The library needs to be configured with your account's secret key which is available in your [Aflorithmic Dashboard](https://console.api.audio). Set aflr.api_key to its value:

```python
import aflr

aflr.api_key = "your-key"
```

## Create Text-to-speech in 3 steps

✍️ Create a new script:

```python
script = aflr.Script().create(scriptText="Hello world")
```

🎤 Create an speech audio file from the script:

```python
response = aflr.Speech().create(scriptId=script["scriptId"])
```

🎉 Finally, get the urls of the audio files generated:

```python
urls = aflr.Speech().retrieve(scriptId=script["scriptId"])
print(urls)
```

Or download the files in your current folder:

```python
aflr.Speech().download(scriptId=script["scriptId"], destination=".")
```

Easy right? Now let's do something fun 🔮

# aflr package Reference

```python
# Retrieve the script item and print the script created

script = aflr.Script().retrieve(scriptId=script["scriptId"])
print(script)

# Retrieve all scripts and print the first's script text

scripts = aflr.Script().list()
print(scripts["scripts"][0]["scriptText"])

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

```
