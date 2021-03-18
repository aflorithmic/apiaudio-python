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
  - [Import](#import)
  - [Authentication](#authentication)
  - [Authentication with environment variable](#authentication_env)
  - [Resource usage](#resource)
  - [Script](#script)
  - [Speech](#speech)
  - [Voice](#voice)
  - [Sound](#sound)
  - [Mastering](#mastering)
  - [File](#file)
- [Authors](#authors)
- [License](#license)

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

# script creation
script = aflr.Script().create(scriptText="Hello world")

# speech creation and retrieval
response = aflr.Speech().create(scriptId=script["scriptId"])
urls = aflr.Speech().retrieve(scriptId=script["scriptId"])
aflr.Speech().download(scriptId=script["scriptId"], destination=".")
```

Now let's run the code:

```sh
python hello.py
```

Once completed, check the files in the `hello.py` root folder - you will see a new audio file. Play it!

## 📑 Documentation <a name = "documentation"></a>

### Import <a name = "import"></a>

```python
import aflr
```

### Authentication <a name = "authentication"></a>

The library needs to be configured with your account's secret key which is available in your [Aflorithmic Dashboard](https://console.api.audio). Set `aflr.api_key` with the api-key you got from the dashboard:

```python
aflr.api_key = "your-key"
```

### Authentication with environment variable (recommended) <a name = "authentication_env"></a>

You can also authenticate using `aflr_key` environment variable and the aflr SDK will automatically use it. To setup, open the terminal and type:

```sh
export aflr_key=<your-key>
```

If you provide both environment variable and `aflr.api_key` authentication, the `aflr.api_key` will be used.

### Resource Usage <a name = "resource"> </a>

There are two approaches to use the resources.
First approach is to get the resource class first, then use resource methods. For example, to create a `Script`, we could do:

```python
Script = aflr.Script()
Script.create()
```

The second approach is to use it directly:

```python
aflr.Script().create()
```

Same logic applies for other resources (`speech`, `voice`, `sound`...)

### `Script` resource <a name = "script"> </a>

The Script resource/class allows you to create, retrieve and list scripts. Learn more about scripts [here](https://docs.api.audio/docs/script-2).

Script methods are:

- `create()` - Create a new script.
  - Parameters:
    - `scriptText` \* [Required] (string) - Text for your script. A script can contain multiple sections and SSML tags. Learn more about scriptText details [here](https://docs.api.audio/docs/script-2)
    - `projectName` (string) - The name of your project. Default value is "default"
    - `moduleName` (string) - The name of your module. Default value is "default"
    - `scriptName` (string) - The name of your script. Default value is "default"
    - `scriptId` (string) - Custom identifier for your script. If scriptId parameter is used, then projectName, moduleName and scriptName are required parameters.
  - Example:
    ```python
    script = aflr.Script().create(
        scriptText="<<sectionName::hello>> Hello {{username|buddy}} <<sectionName::bye>> Good bye from {{location|barcelona}}",
        projectName="myProject",
        moduleName="myModule",
        scriptName="myScript",
        scriptId="id-1234"
        )
    ```
- `retrieve()` - Retrieve a script by id.
  - Parameters:
    - `scriptId` \* [Required] (string) - The script ID you want to retrieve.
  - Example:
    ```python
    script = aflr.Script().retrieve(scriptId="id-1234")
    ```
- `list()` - List all scripts available in your organization.
  - Parameters:
    - No parameters required.
  - Example:
    ```python
    scripts = aflr.Script().list()
    ```

### `Speech` resource <a name = "speech"> </a>

Speech allows you to do Text-To-Speech (TTS) with our API using all the voices available. Use it to create a speech audio file from your script.

Speech methods are:

- `create()` Send a Text-To-Speech request to our Text-To-Speech service.
  - Parameters:
    - `scriptId` \* [Required] (string) - The script ID
    - `voiceName` (string) - Voice name. See the list of available voices using [Voice resource](#voice). Default voiceName is "Joanna"
    - `voiceProvider` (string) - Voice name. See the list of available voices and voice providers using [Voice resource](#voice). Default voiceProvider is "polly"
    - `scriptSpeed` (string) - Voice speed. Default speed is 100.
  - Example:
    ```python
    response = aflr.Speech().create(
        scriptId="id-1234",
        voiceName="Joanna",
        voiceProvider="polly",
        scriptSpeed="100"
        )
    ```
- `retrieve()` Retrieve the speech file urls.
  - Parameters:
    - `scriptId` \* [Required] (string) - The script ID you want to retrieve.
  - Example:
    ```python
    audio_files = aflr.Speech().retrieve(scriptId="id-1234")
    ```
- `download()` Download the speech files in your preferred folder.
  - Parameters:
    - `scriptId` \* [Required] (string) - The script ID you want to download
    - `destination` (string) - The folder destination path. Default is "." (current folder)
  - Example:
    ```python
    audio_files = aflr.Speech().download(scriptId="id-1234", destination=".")
    ```

### `Voice` resource <a name = "voice"> </a>

Voice allows you to retrieve a list of the available voices from our API.

Voice methods are:

- `list()` List all the available voices in our API.
  - Parameters:
    - No parameters required.
  - Example:
    ```python
    all_voices = aflr.Voice().list()
    ```

### `Sound` resource <a name = "sound"> </a>

Sound allows you to design your own sound template from a script and a background track. In order to get a sound template/project, make sure you requested [speech](#speech) for your script resource first.

Sound methods are:

- `create()` Creates a sound template, compresses the sound project into a zip file and returns the url.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `backgroundTrackId` \* [Required] (string) - The background track file ID.
  - Example:
    ```python
    sound_url = aflr.Sound().create(
        scriptId="id-1234",
        backgroundTrackId="full__citynights.wav",
    )
    ```
- `retrieve()` Retrieve the url of the sound project zip file.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
  - Example:
    ```python
    audio_files = aflr.Sound().retrieve(scriptId="id-1234")
    ```
- `download()` Download the sound project zip file in your preferred folder.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `destination` (string) - The folder destination path. Default is "." (current folder)
  - Example:
    ```python
    audio_files = aflr.Sound().download(scriptId="id-1234", destination=".")
    ```

### `Mastering` resource <a name = "mastering"> </a>

Mastering allows you to create and retrieve a mastered audio file of your script. A mastered version contains the speech of the script, a background track, personalised parameters for your audience and a mastering process to enhance the audio quality of the whole track. In order to get a mastered audio file, make sure you requested [speech](#speech) for your script resource first.

Mastering methods are:

- `create()` Creates a mastered version of your script.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `backgroundTrackId` \* [Required] (string) - The background track file ID.
    - `audience` (list) - List of dicts containing the personalisation parameters. This parameter depends on the number of parameters you used in your [script](#script) resource. In the script documentation example above, we used 2 parameters: `username` and `location`, and in the following example below we want to produce the script for username `Antonio` with location `Barcelona`.
  - Example:
    ```python
    response = aflr.Mastering().create(
        scriptId="id-1234",
        backgroundTrackId="full__citynights.wav",
        audience = [{"username":"antonio", "location":"barcelona"}]
    )
    ```
- `retrieve()` Retrieves the mastered file urls.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
  - Example:
    ```python
    mastered_files = aflr.Mastering().retrieve(scriptId="id-1234")
    ```
- `download()` Download the mastered files in your preferred folder.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `destination` (string) - The folder destination path. Default is "." (current folder)
  - Example:
    ```python
    mastered_files = aflr.Mastering().download(scriptId="id-1234", destination=".")
    ```

### `File` resource <a name = "file"> </a>

File allows you to retrieve all the files available in api.audio for your organization.

Available soon.

# Authors <a name = "authors"> </a>

- https://github.com/tonythree
- https://github.com/GetOn4
- https://github.com/zeritte

# License <a name = "license"> </a>

This project is licensed under the terms of the MIT license.
