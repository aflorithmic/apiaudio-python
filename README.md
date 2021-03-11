# aflr

aflr is the official [api.audio](https://www.api.audio) Python SDK. This SDK provides easy access to the api.audio API from applications written in python.

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

Easy right? Now let's add some music! 🔮

## Create

# aflr package Reference

## Script

```python

## CREATE SCRIPT
# Create a script item with two sections (hello, bye) & 2 personalisation parameters (username, location).
# Scripts can have any number of sections.
# Every section will be a separated speech file.
# A script will always follow a hierarchical structure: project/module/script.
# Only required parameter is scriptText.
# projectName, moduleName and scriptName are optional.
# If not provided, projectName, moduleName and scriptName will be "default".
# scriptId is optional.
script = aflr.Script().create(
    scriptText="<<sectionName::hello>> Hello {{username|buddy}} <<sectionName::bye>> Good bye from {{location|barcelona}}",
    projectName="myProject",
    moduleName="myModule",
    scriptName="myScript",
    scriptId="id-1234"
    )
print(script)

## RETRIEVE SCRIPT
# Retrieve the script item and print the script created.
# Required parameter: scriptId
script = aflr.Script().retrieve(scriptId=script["scriptId"])
print(script)

## LIST SCRIPTS
# Retrieve all scripts in your organization and print the list of scripts.
# List does not require any parameter.
# print the scriptText from the first script item found.
scripts = aflr.Script().list()
print(scripts)
print(scripts["scripts"][0]["scriptText"])

```

## Speech

```python
# create a text-to-speech

response = aflr.Speech().create(scriptId=script["scriptId"])
print(response)

# get the speech audio files

audio_files = aflr.Speech().retrieve(scriptId=script["scriptId"])
print(audio_files)

# download all speech audio files
aflr.Speech().download(scriptId=script["scriptId"], destination=".")

# check your folder :) you should have the following audio_files

audio_files = aflr.Speech().download(scriptId=script["scriptId"], destination=".")
print(audio_files)
```

## Voice

```python
# Get all available voices and print the first one

all_voices = aflr.Voice().list()
print(all_voices["voices"][0])

```
