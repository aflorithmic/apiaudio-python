<p align="center">
<a href="https://www.api.audio/" rel="noopener">
 <img src="https://uploads-ssl.webflow.com/60b89b300a9c71a64936aafd/60c1d07f4fd2c92916129788_logoAudio.svg" alt="api.audio logo"></a>
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

### Create Text to audio in 4 steps

Let's create our first audio from text.

✍️ Create a new script:

```python
script = aflr.Script.create(scriptText="Hello world", scriptName="hello")
print(script)
```

🎤 Create an speech audio file from the script using Joanna's voice:

```python
response = aflr.Speech.create(scriptId=script["scriptId"], voice="Joanna")
print(response)
```

🎧 Now let's master the speech file with high quality and a nice background track.

```python
response = aflr.Mastering.create(
	scriptId=script.get("scriptId"),
	backgroundTrackId="full__citynights.wav"
	)
print(response)
```

🎉 Finally, get the urls of the audio files generated:

```python
urls = aflr.Mastering.retrieve(scriptId=script["scriptId"])
print(urls)
```

Or download the files in your current folder:

```python
filepath = aflr.Mastering.download(scriptId=script["scriptId"], destination=".")
print(filepath)
```

Easy right? 🔮 This is the `hello.py` final picture:

```python
import aflr
aflr.api_key = "your-key"

# script creation
script = aflr.Script.create(scriptText="Hello world", scriptName="hello")

# speech creation
response = aflr.Speech.create(scriptId=script["scriptId"], voice="Joanna")
print(response)

# mastering process
response = aflr.Mastering.create(
	scriptId=script.get("scriptId"),
	backgroundTrackId="full__citynights.wav"
	)
print(response)

# get url of audio tracks generated
urls = aflr.Mastering.retrieve(scriptId=script["scriptId"])
print(urls)

# or download
filepath = aflr.Mastering.download(scriptId=script["scriptId"], destination=".")
print(filepath)
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
First approach is to import the resource classes you want to use first, then use resource methods. For example, to use `Script`, we could do:

```python
from aflr import Script
Script.create()
```

The second approach is to use it directly from aflr:

```python
import aflr
aflr.Script.create()
```

Same logic applies for other resources (`Speech`, `Voice`, `Sound`...)

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
    script = aflr.Script.create(
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
    script = aflr.Script.retrieve(scriptId="id-1234")
    ```
- `list()` - List all scripts available in your organization.
  - Parameters:
    - No parameters required.
  - Example:
    ```python
    scripts = aflr.Script.list()
    ```
- `get_random_text()` - Retrieve random text from a list of categories.
  - Parameters:
    - `category` (string) - The category from which the random text is retrieved. If no category is specified, the function defaults to `"FunFact"`
  - Example:
    ```python
    text = aflr.Script.get_random_text(category="BibleVerse")
    ```
    - Categories currently available: `"BibleVerse"`, `"FunFact"`, `"InspirationalQuote"`, `"Joke"`, `"MovieSynopsis"`, `"Poem"`, `"PhilosophicalQuestion"`, `"Recipe"`, `"TriviaQuestion"`.
    
### `Speech` resource <a name = "speech"> </a>

Speech allows you to do Text-To-Speech (TTS) with our API using all the voices available. Use it to create a speech audio file from your script.

Speech methods are:

- `create()` Send a Text-To-Speech request to our Text-To-Speech service.
  - Parameters:
    - `scriptId` \* [Required] (string) - The script ID
    - `voice` (string) - Voice name. See the list of available voices using [Voice resource](#voice). Default voice is "Joanna".
    - `speed` (string) - Voice speed. Default speed is 100.
    - `effect` (string) - Put a funny effect in your voice. You can try the following ones: `dark_father`, `chewie`, `88b`, `2r2d`
    - `silence_padding` (integer) - Add a silence padding to your speech tracks (in milliseconds). Default is 0 (no padding)
    - `audience` (dictionary) - List of dicts containing the personalisation parameters as key-value pairs. This parameter depends on the number of parameters you used in your script resource. For instance, if in the script resource you have `scriptText="Hello {{name}} {{lastname}}"`, the audience should be: `[{"username": "Elon", "lastname": "Musk"}]`
    - `sections` (dictionary) is a dictionary (key-value pairs), where the key is a section name, and the value is another dictionary with the section configuration ( valid parameters are: voice, speed, effect, silence_padding). If a section is not found here, the section will automatically inherit the voice, speed, effect and silence_padding values you defined above (or the default ones if you don't provide them). See an example below with 2 sections and different configuration parameters being used.
      ```python
      sections={
          "firstsection": {
              "voice": "Matthew",
              "speed": 110,
              "silence_padding": 100,
              "effect": "dark_father"
          },
          "anothersection": {
              "voice": "en-GB-RyanNeural",
              "speed": 100
          }
      }
      ```
    - `voiceName` (DEPRECATED, use `voice` instead)
    - `scriptSpeed`(DEPRECATED, use `speed` instead)
  - Simple example:
    ```python
    response = aflr.Speech.create(
        scriptId="id-1234",
        voice="Joanna"
        )
    ```
  - Complete example:
    ```python
    response = aflr.Speech.create(
        scriptId="id-1234",
        voice="Matthew",
        speed=100,
        effect="dark_father",
        silence_padding= 1000,
        audience=[{"username": "Elon", "lastname": "Musk"}],
        sections={
            "firstsection": {
                "voice": "Matthew",
                "speed": 110,
                "silence_padding": 100,
                "effect": "dark_father"
            },
            "anothersection": {
                "voice": "en-GB-RyanNeural",
            }
        }
    )
    ```
- `retrieve()` Retrieve the speech file urls.

  - Parameters:
    - `scriptId` \* [Required] (string) - The script ID you want to retrieve.
    - `section` (string) - The script section name for the first section. The default name for a script section is "default". NOTE: At the moment, Only scripts with 1 section are supported. If the scripts contain more than one section, only the first section can be retrieved.
    - `parameters` (dict) - Dict containing the personalisation parameters for the first section of the script. This parameter depends on the parameters you used in your [script](#script)'s resource section. If this parameter is used, `section` must be specified.
  - Example:
    ```python
    audio_files = aflr.Speech.retrieve(scriptId="id-1234")
    ```

- `download()` Download the speech files in your preferred folder.
  - Parameters:
    - `scriptId` \* [Required] (string) - The script ID you want to download
    - `section` (string) - The script section name for the first section. The default name for a script section is "default". NOTE: At the moment, Only scripts with 1 section are supported. If the scripts contain more than one section, only the first section can be retrieved.
    - `parameters` (dict) - Dict containing the personalisation parameters for the first section of the script. This parameter depends on the parameters you used in your [script](#script)'s resource section. If this parameter is used, `section` must be specified.
    - `destination` (string) - The folder destination path. Default is "." (current folder)
  - Example:
    ```python
    audio_files = aflr.Speech.download(scriptId="id-1234", destination=".")
    ```

### `Voice` resource <a name = "voice"> </a>

Voice allows you to retrieve a list of the available voices from our API.

Voice methods are:

- `list()` List all the available voices in our API. The parameters are all optional, and can be used in combination to get the perfect voice for your usecase.

  - Parameters:
    - `provider` (string) - Try one of: google, polly, azure, msnr
    - `providerFullName` (string) - Try with one of: amazon polly, google, microsoft azure, aflorithmic labs
    - `language` (string) - Try with one of: english, spanish, french, german
    - `accent` (string) - Try with one of: american, british, neutral, portuguese/brazilian, american soft, mexican, australian
    - `gender` (string) - Try with one of: male, female
    - `ageBracket` (string) - Try with one of: adult, child, senior
    - `tags` (string) - Try with one or more (separated by commas) of: steady, confident, balanced, informative, serious, instructional, slow, storytelling, calm, clear, deep, formal, sad, thin, fast, upbeat, fun, energetic, tense, very fast, flat, low pitched, high pitched, low-pitched, sing-y, cooperative, kind, stable, monotonous, neutral, responsible, business man, straight to the point, knowledgeable, focused, newscastery, newsreader, interviewer, reliable, friendly, welcoming, good for handing out information, slightly friendly
    - `industryExamples` (string) - Try with one or more (separated by commas) of: fitness, business, commercial, fashion, travel, audiobook, real estate, faith, health industry, comercial, realestate, kids entertainment, games, customer service, education, storytelling, entertainment, kids, education audiobook
  - Example:
    ```python
    all_voices = aflr.Voice.list()
    ```
  - Example:
    ```python
    french_voices = aflr.Voice.list(language="french",tags="steady, fun")
    ```

- `list_parameters()` This endpoint lets you see which attributes you can filter the voices by, along with the allowed values for each attribute. You can later use these parameters and values to filter the voices you wish to list.

  - Parameters:

    - No parameters required.

  - Example:
    ```python
    parameters = aflr.Voice.list_parameters()
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
    sound_url = aflr.Sound.create(
        scriptId="id-1234",
        backgroundTrackId="full__citynights.wav",
    )
    ```
- `retrieve()` Retrieve the url of the sound project zip file.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
  - Example:
    ```python
    audio_files = aflr.Sound.retrieve(scriptId="id-1234")
    ```
- `list_sound_templates()` List all the available sound templates in our api.
  - Parameters:
    - No parameters required.
  - Example:
    ```python
    sound_templates = aflr.Sound.list_sound_templates()
    ```
- `list()` List all the available background tracks in our API.
  - Parameters:
    - No parameters required.
  - Example:
    ```python
    all_bg_tracks = aflr.Sound.list()
    ```
- `list_v2()` List all the available background tracks in our API including a 15 seconds audio snippet.
  - Parameters:
    - No parameters required.
  - Example:
    ```python
    all_bg_tracks = aflr.Sound.list_v2()
    ```
- `download()` Download the sound project zip file in your preferred folder.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `destination` (string) - The folder destination path. Default is "." (current folder)
  - Example:
    ```python
    audio_files = aflr.Sound.download(scriptId="id-1234", destination=".")
    ```

### `Mastering` resource <a name = "mastering"> </a>

Mastering allows you to create and retrieve a mastered audio file of your script. A mastered version contains the speech of the script, a background track, personalised parameters for your audience and a mastering process to enhance the audio quality of the whole track. In order to get a mastered audio file, make sure you requested [speech](#speech) for your script resource first.

Mastering methods are:

- `create()` Creates a mastered version of your script.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `backgroundTrackId` \* [Required] (string) - The background track file ID.
    - `audience` (list) - List of dicts containing the personalisation parameters. This parameter depends on the number of parameters you used in your [script](#script) resource. In the script documentation example above, we used 2 parameters: `username` and `location`, and in the following example below we want to produce the script for username `Antonio` with location `Barcelona`.
    - `public` (boolean) - Boolean flag that allows to store the mastered file in a public s3 folder. Default value is `False`. Warning - This will cause your mastered files to be public to anyone in the internet. Use this at your own risk.
    - `vast` (boolean) - Boolean flag that allows to create a VAST file of your mastered file. The `vast` flag only works if `public` is `True`. Default value is `False`.
  - Example:
    ```python
    response = aflr.Mastering.create(
        scriptId="id-1234",
        backgroundTrackId="full__citynights.wav",
        audience=[{"username":"antonio", "location":"barcelona"}]
    )
    ```
- `retrieve()` Retrieves the mastered file urls.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `parameters` (dict) - Dictionary containing the audience item you want to retrieve.
    - `public` (boolean) - Boolean flag that allows to retrieve the mastered file from the public bucket. Use this if you want to retrieve a mastered file created using `public=True`. Default value is `False`.
    - `vast` (boolean) - Boolean flag that allows to retrieve the VAST file of your mastered file. The `vast` flag only works if `public` is `True`. Default value is `False`.
  - Example:
    ```python
    mastered_files = aflr.Mastering.retrieve(
      scriptId="id-1234",
      parameters={"username":"antonio", "location":"barcelona"}
    )
    ```
- `download()` Download the mastered files in your preferred folder.
  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `parameters` (dict) - Dictionary containing the audience item you want to retrieve.
    - `destination` (string) - The folder destination path. Default is "." (current folder)
  - Example:
    ```python
    mastered_files = aflr.Mastering.download(
      scriptId="id-1234",
      parameters={"username":"antonio", "location":"barcelona"}
      destination="."
    )
    ```

### `File` resource <a name = "file"> </a>

File allows you to retrieve all the files available in api.audio for your organization.

Available soon.

# Authors <a name = "authors"> </a>

- https://github.com/tonythree
- https://github.com/GetOn4
- https://github.com/zeritte
- https://github.com/springcoil
- https://github.com/a96lex

# License <a name = "license"> </a>

This project is licensed under the terms of the MIT license.
