<p align="center">
<a href="https://www.api.audio/" rel="noopener">
 <img src="https://d9hhrg4mnvzow.cloudfront.net/www.api.audio/ddeb49ef-logo-api-audio-isolines_10au02y000000000000028.png" alt="api.audio logo"></a>
</p>

<h3 align="center">aflr - python SDK</h3>

---

<p align="center"> aflr is the official <a href="https://www.api.audio/" rel="noopener">api.audio</a> Python 3 SDK. This SDK provides easy access to the api.audio API from applications written in python. 
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Hello World](#hello_world)
- [Documentation](#documentation)
- [Reference](#reference)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This repository is actively maintained by [Aflorithmic Labs](https://www.aflorithmic.ai/). For examples, recipes and api reference see the [api.audio docs](https://docs.api.audio/reference).

## 🏁 Getting Started <a name = "getting_started"></a>

### Installation

You don't need this source code unless you want to modify it. If you want to use the package, just run:

```sh
pip install aflr -U
```

Install from source with:

```sh
python setup.py install
```

### Prerequisites <a name = "requirements"></a>

Python 3.6+

## 🚀 Hello World <a name = "hello_world"></a>

Create a file `hello.py`

```python
touch hello.py
```

### Authentication

The library needs to be configured with your account's secret key which is available in your [Aflorithmic Dashboard](https://console.api.audio). Import the aflr package and set `aflr.api_key` with the api-key you got from the dashboard:

```python
import aflr
aflr.api_key = "your-key"
```

### Create Text-to-speech in 3 steps

Let's create our first speech from text.

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

Easy right? 🔮 This is the `hello.py` final picture:
```python
import aflr
aflr.api_key = "your-key"

script = aflr.Script().create(scriptText="Hello world")
response = aflr.Speech().create(scriptId=script["scriptId"])
urls = aflr.Speech().retrieve(scriptId=script["scriptId"])
aflr.Speech().download(scriptId=script["scriptId"], destination=".")
```

## 📑 Documentation <a name = "documentation"></a>

### `Script` resource

The Script resource allows you to create, retrieve and list scripts. Script is a class, and have different methods you can use:

- `create()` Create a new script.
- `retrieve()` Retrieve a script by id.
- `list()` List all scripts available in your organization.

There are two approaches to use the `Script` resource.
First approach is to get the Script class first, then use Script methods. For example, to create a `Script`, we could do:

```python
Script = aflr.Script()
Script.create()
```

or simply:

```python
aflr.Script().create()
```

### Speech

Coming soon.

### Voice

Coming soon.

### Sound

Coming soon.

### File

Coming soon.

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
audio_files = aflr.Speech().download(scriptId=script["scriptId"], destination=".")

# check your folder :) you should have the following audio_files
print(audio_files)


```

## Voice

```python
# Get all available voices and print the first one

all_voices = aflr.Voice().list()
print(all_voices["voices"][0])

```
