# api.audio Python SDK

The Aflorithmic api.audio Python SDK "aflr" provides access to the api.audio API from applications written in python.

## Documentation

See the [Python API docs](https://docs.api.audio/reference)

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

# Usage

The library needs to be configured with your account's secret key which is available in your [Aflorithmic Dashboard](http://ms-api-frontend.s3-website-eu-west-1.amazonaws.com/). Set aflr.api_key to its value:

```python
import aflr

aflr.api_key = "your-key"

# Create a new script and print the script created
script = aflr.Script().create(
    scriptText="<<sectionName::hello>> Hello world"
)
print(script)

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
