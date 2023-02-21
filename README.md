## This repo is no longer in activate development, please use the [audiostack SDK](https://pypi.org/project/audiostack/) to continue using api.audio.

<p align="center">
<a href="https://www.api.audio/" rel="noopener">
 <img src="https://uploads-ssl.webflow.com/60b89b300a9c71a64936aafd/60c1d07f4fd2c92916129788_logoAudio.svg" alt="api.audio logo"></a>
</p>

<h3 align="center">apiaudio - python SDK</h3>

---

<p align="center"> apiaudio is the official <a href="https://www.api.audio/" rel="noopener">api.audio</a> Python 3 SDK. This SDK provides easy access to the api.audio API for applications written in python.
    <br>
</p>

## 📝 Table of Contents

- [Changelog](CHANGELOG.md)
- [About](#about)
- [Changelog](#changelog)
- [Quickstarts](#quickstarts)
- [Getting Started](#getting_started)
- [Hello World](#hello_world)
- [Documentation](#documentation)
  - [Import](#import)
  - [Authentication](#authentication)
  - [Authentication with environment variable](#authentication_env)
  - [Super Organizations](#super-organizations)
  - [Resource usage](#resource)
  - [Organization](#organization)
  - [Script](#script)
    - [Directory](#directory)
  - [Speech](#speech)
  - [Voice](#voice)
  - [Sound](#sound)
  - [Mastering](#mastering)
  - [Media](#media)
  - [SyncTTS](#synctts)
  - [Birdcache](#birdcache)
  - [Pronunciation Dictionary](#pronunciationdictionary)
  - [Connector](#connector)
  - [Orchestrator](#orchestrator)
  - [Webhooks](#webhooks)
  - [Logging](#logging)
- [Maintainers](#maintainers)
- [License](#license)

## 🧐 About <a name = "about"></a>

This repository is actively maintained by [Aflorithmic Labs](https://www.aflorithmic.ai/). For examples, recipes and api reference see the [api.audio docs](https://docs.api.audio/reference). Feel free to get in touch with any questions or feedback!

## :book:  Changelog

You can view [here](CHANGELOG.md) our updated Changelog.

## :speedboat:  Quickstarts <a name = "quickstarts"></a>

Get started with our [quickstart recipes](https://github.com/aflorithmic/examples).

## 🏁 Getting Started <a name = "getting_started"></a>

### Installation

You don't need this source code unless you want to modify it. If you want to use the package, just run:

```sh
pip install apiaudio -U
#or
pip3 install apiaudio -U
```

Install from source with:

```sh
python setup.py install
#or
python3 setup.py install
```

### Prerequisites <a name = "requirements"></a>

Python 3.6+

## 🚀 Hello World <a name = "hello_world"></a>

Create a file `hello.py`

```python
touch hello.py
```

### Authentication

This library needs to be configured with your account's api-key which is available in your [api.audio Console](https://console.api.audio). Import the apiaudio package and set `apiaudio.api_key` with the api-key you got from the console:

```python
import apiaudio
apiaudio.api_key = "your-key"
```


### Create Text to audio in 4 steps

Let's create our first audio asset.

✍️ Create a new script, our `scriptText` will be the text that is later synthesized.

```python
script = apiaudio.Script.create(scriptText="Hello world")
print(script)
```

🎤 Render the scriptText that was created in the previous step. Lets use voice Aria.

```python
response = apiaudio.Speech.create(scriptId=script["scriptId"], voice="Aria")
print(response)
```

🎧 Now let's join the speech we just created with a sound template.

```python
response = apiaudio.Mastering.create(
	scriptId=script.get("scriptId"),
	soundTemplate="jakarta"
	)
print(response)
```

Download the final audio asset to your current working directory:

```python
filepath = apiaudio.Mastering.download(scriptId=script["scriptId"], destination=".")
print(filepath)
```

Easy right? 🔮 This is the final `hello.py` file.

```python
import apiaudio
apiaudio.api_key = "your-key"

# script creation
script = apiaudio.Script.create(scriptText="Hello world")

# speech creation
response = apiaudio.Speech.create(scriptId=script["scriptId"], voice="Aria")

print(response)

# mastering process
response = apiaudio.Mastering.create(
	scriptId=script.get("scriptId"),
	soundTemplate="jakarta"
	)
print(response)

# download
filepath = apiaudio.Mastering.download(scriptId=script["scriptId"], destination=".")
print(filepath)
```

Now let's run the code:

```sh
python hello.py
#or
python3 hello.py
```

Once this has completed, find the downloaded audio asset and play it! :sound: :sound: :sound: 

## 📑 Documentation <a name = "documentation"></a>

### Import <a name = "import"></a>

```python
import apiaudio
```

### Authentication <a name = "authentication"></a>

The library needs to be configured with your account's secret key which is available in your [Aflorithmic Dashboard](https://console.api.audio). Set `apiaudio.api_key` with the api-key you got from the dashboard:

```python
apiaudio.api_key = "your-key"
```

### Authentication with environment variable (recommended) <a name = "authentication_env"></a>

You can also authenticate using `apiaudio_key` environment variable and the apiaudio SDK will automatically use it. To setup, open the terminal and type:

```sh
export apiaudio_key=<your-key>
```

If you provide both an environment variable and `apiaudio.api_key` authentication value, the `apiaudio.api_key` value will be used instead.

### Super Organizations

In order to control a child organization of yours, please use the following method to *assume* that organization id.

Set your child organization id to `None` to stop assuming an organization. Subsequent calls to the api will use your own organization id.

```python
import apiaudio

apiaudio.set_assume_org_id('child_org_id')

# Stop using
apiaudio.set_assume_org_id(None)
```

See [organization](#organization) resource for more operations you can perform about your organization.

### Resource Usage <a name = "resource"> </a>

There are two approaches to use the resources.

The recommended approach is to import all resources directly from apiaudio:

```python
import apiaudio
apiaudio.Script.create()
```


Alternatively, you can import the resource classes you want to use first, and then use the resource methods. For example, to use `Script`, we could do:

```python
from apiaudio import Script
Script.create()
```


Same logic applies for other resources (`Speech`, `Voice`, `Sound`...)

### `Organization` resource <a name = "organization"> </a>

The Organization resource/class allows you to perform some data retrieval about your organization and your child organizations.

Organization methods are:

- `get_org_data()` - Get organizations data, including orgId, orgName etc.
  - Parameters:
    - None.
  - Example:
    ```python
    org_data = apiaudio.Organization.get_org_data()
    ```
- `list_child_orgs()` - List your child organizations.
  - Parameters:
    - None.
  - Example:
    ```python
    child_orgs = apiaudio.Organization.list_child_orgs()
    ```
- `get_secrets()` - Get your api key, webhook url and webhook secret.
  - Parameters:
    - None.
  - Example:
    ```python
    secrets = apiaudio.Organization.get_secrets()
    ```

### `Script` resource <a name = "script"> </a>

The Script resource/class allows you to create, retrieve and list scripts. Learn more about scripts [here](https://docs.api.audio/docs/script-2).

Script methods are:

- `create()` - Create a new script.
  - Parameters:
    - `scriptText` \* [Required] (string) - Text for your script. A script can contain multiple sections and SSML tags. Learn more about scriptText details [here](https://docs.api.audio/docs/script-2)
    - `projectName` (string) - The name of your project. Default value is "default" (max 60 characters)
    - `moduleName` (string) - The name of your module. Default value is "default" (max 60 characters)
    - `scriptName` (string) - The name of your script. Default value is "default" (max 60 characters)
    - `scriptId` (string) - Custom identifier for your script. If scriptId parameter is provided, then projectName, moduleName and scriptName are set to the same value as scriptId
    - `versions` (dictionary) - A dictionary containing different versions of your script text, whereby the key is the version name, and its value is the associated `scriptText`. Version name `v0` is reserved as the default `scriptText`. Default value is "{}"
    - `metadata` (dictionary) - Metadata for your script. This is limited to 2kb in size.
  - Example:
    ```python
    text = """
      <<sectionName::hello>> Hello {{username|buddy}} 
      <<sectionName::bye>> Good bye from {{location|barcelona}}
    """
    
    script = apiaudio.Script.create(
        scriptText=text,
        projectName="myProject",
        moduleName="myModule",
        scriptName="myScript",
        scriptId="id-1234",
        metadata={"author" : "sam", "tags" : ["demo", "intro"]}
        )
    # example 2 with versions
    script = apiaudio.Script.create(
        scriptText="Default text",
        versions={"es" : "Hola", "en" : "hello"}
        )
    ```
- `retrieve()` - Retrieve a script by id.
  - Parameters:
    - `scriptId` \* [Required] (string) - The script ID you want to retrieve. By default retrieves the main version (v0).
    - `version` (string) - The script version you want to retrieve.
  - Example:
    ```python
    script = apiaudio.Script.retrieve(scriptId="id-1234", version="abc")
    ```
- `preview` - return a script with the dictionary highlighting applied. see [Lexi](#lexi) for more examples of how to use the dictionary feature.

  - Parameters:

    - `scriptId` \* [Required] (string) - The script ID you want to use.
    - `voice` \* [Required] (string) - The voice that will be used to render speech. This is required as the output can be dependent on voice, language code, or provider.

  - Example:

  ```python
    text = """
      The author of this repo has lived in two places in the
      UK, <!location>Bude<!> and <!location>Bristol<!>.
    """

  r = apiaudio.Script.create(scriptText=text)
  scriptId = r["scriptId"]

  preview = apiaudio.Script.preview(scriptId=scriptId, language="en-gb")
  ```

- `list()` - List all scripts available in your organization. This method supports filtering.
  - Parameters:
    - `projectName` (string) - Return any scripts with this projectName.
    - `moduleName` (string) - Return any scripts with this moduleName, note `projectName` also needs to be supplied.
    - `scriptName` (string) - Return any scripts with this scriptName, not both `projectName` and `moduleName` need to be supplied.
    - `scriptId` (string) - Return any scripts with this scriptId.
    - `verbose` (bool) - List scripts in verbose mode (`True` by default). Set this to `False` to return only the `projectName`, `moduleName`, `scriptName` and `scriptId` fields.
  - Example:
    ```python
    scripts = apiaudio.Script.list()
    ```
- `delete()` - Deletes a script. By default this will delete all versions of the script.
  - Parameters:
    - `scriptId` \* [Required] (string) - The id of the script to be deleted
    - `version` (string) - Delete a specific version.
  - Example:
    ```python
    #deletes version 'en' from scriptId 'myworkout'
    scripts = apiaudio.Script.delete(scriptId="myworkout", version="en")
    ```
- `delete_multiple()` - Delete multiple scripts.
  - Parameters:
    - `projectName` \* [Required] (string) - Deletes all scripts within this projectName.
    - `moduleName` (string) - Deletes all scripts within this moduleName, note `projectName` also needs to be supplied.
    - `scriptName` (string) - Deletes all scripts within this scriptName, note both `projectName` and `moduleName` need to be supplied.

  - Example:
    ```python
    #deletes all scripts within the project 'awesome_demos'
    scripts = apiaudio.Script.delete_multiple(projectName="awesome_demos")
    ```

- `get_random_text()` - Retrieve random text from a list of categories.
  - Parameters:
    - `category` (string) - The category from which the random text is retrieved. If no category is specified, the function defaults to `"FunFact"`
  - Example:
    ```python
    text = apiaudio.Script.get_random_text(category="BibleVerse")
    ```
    - Categories currently available: `"BibleVerse"`, `"FunFact"`, `"InspirationalQuote"`, `"Joke"`, `"MovieSynopsis"`, `"Poem"`, `"PhilosophicalQuestion"`, `"Recipe"`, `"TriviaQuestion"`.
  #### `Script.Directory` resource <a name = "directory"> </a>

  Lists the directory structure of your scripts, i.e. projectName/moduleName/scriptName

  Script.Directory methods are:

  - `list_projects()` - Lists all projects.
  - Parameters:
    - none

  - Example:
    ```python
    #Lists all project names
    projects = apiaudio.Script.Directory.list_projects()
    print(projects)
    # example output: ["projectX", "projectY"]
    ```

  - `list_modules()` - Lists all modules within a projectPrefix.
  - Parameters:
    - `projectPrefix` \* [Required] - will list modules starting with this projectPrefix.

  - Example:
    ```python
    #Lists all module names
    modules = apiaudio.Script.Directory.list_modules(projectPrefix="workout")

    print(modules)
    # example output: ["workout_1/over60s", "workout_2/morning_routine"]
    ```

  - `list_script_names()` - Lists all modules within a projectPrefix.
  - Parameters:
    - `projectPrefix` \* [Required] - will list scriptNames starting with this projectPrefix.
    - `modulePrefix` \* [Required] - will list scriptNames starting with this modulePrefix.

  - Example:
    ```python
    #Lists all script names
    scriptNames = apiaudio.Script.Directory.list_script_names(projectPrefix="workout_1", modulePrefix="over60s")

    print(scriptNames)
    # example output: ["workout_1/over60s/routine_1", "workout_1/over60s/routine_2", "workout_1/over60s/routine_3"]
    ```


### `Speech` resource <a name = "speech"> </a>

Speech allows you to do Text-To-Speech (TTS) with our API using all the voices available. Use it to create a speech audio file from your script.

Speech methods are:

- `create()` Send a Text-To-Speech request to our Text-To-Speech service.

  - Parameters:

    - `scriptId` \* [Required] (string) - The script ID
    - `version` (string) - The version of the script to be produced. Default is "".
    - `voice` (string) - Voice name. See the list of available voices using [Voice resource](#voice). Default voice is "Joanna".
    - `speed` (string) - Voice speed. Default speed is 100.
    - `effect` (string) - Put a funny effect in your voice. You can try the following ones: `dark_father`, `chewie`, `88b`, `2r2d`,
    - `silencePadding` (integer) - Add a silence padding to your speech tracks (in milliseconds). Default is 0 (no padding)
    - `audience` (dict) - Specify the values of parameters in your script. For instance, if in the script resource you have `scriptText="Hello {{name}} {{lastname}}, welcome to {{location}}"`, the audience should be: `{"name": "Elon", "lastname": "Musk", "location": "Istanbul"}`. If not provided, the fallback track will be created.
    - `sync` (boolean) - Allow sync or async speech creation. Default is `True`. If `sync=False`, speech create call will return a success message when the speech creation is triggered. To retrieve the files, check `Speech.retrieve()` method.
    - `sections` (dict) - Specify parameters for specific sections in the script. The key is a section name, and the value is another dictionary with the section configuration ( valid parameters are: voice, speed, effect, silence_padding). If a section is not found here, the section will automatically inherit the voice, speed, effect and silence_padding values you defined above (or the default ones if you don't provide them). See an example below with 2 sections and different configuration parameters being used.
    - `useDictionary` (bool) - Applies pronunciation dictionary to the script text.
    - `useTextNormalizer` (bool) - Applies text normalization, which can help resolve grammatical errors with TTS pronunciations, for example 11:12 Uhr -> 11 Uhr 12. Note - this only works for german voices at present.
      ```python
      sections={
          "firstsection": {
              "voice": "Matthew",
              "speed": 110,
              "silence_padding": 100
          },
          "anothersection": {
              "voice": "en-GB-RyanNeural",
              "speed": 100
          }
      }
      ```

  - Simple example:
    ```python
    response = apiaudio.Speech.create(
        scriptId="id-1234",
        voice="Joanna"
        )
    ```
  - Complete example:
    ```python
    response = apiaudio.Speech.create(
        scriptId="id-1234",
    version="abc",
        voice="Matthew",
        speed=100,
        effect="dark_father",
        silencePadding= 1000,
        sync=True,
        audience={"username": "Elon", "lastname": "Musk"},
        sections={
            "firstsection": {
                "voice": "Matthew",
                "speed": 110,
                "silence_padding": 100,
            },
            "anothersection": {
                "voice": "Liam",
            }
        }
    )
    ```

- `retrieve()` Retrieve the speech file urls.

  - Parameters:

    - `scriptId` \* [Required] (string) - The script ID you want to retrieve.
    - `version` (string) - The version of the script to be retrieved. Default is "".
    - `section` (string) - The script section name you want to retrieve. If not provided, all the script sections will be returned.
    - `parameters` (dict) - Dict containing the personalisation parameters of your script. If not provided, the fallback track will be retrieved. This field depends on the parameters you used in your [script](#script)'s resource section. In order to retrieve a specific set of parameters, you need to create the speech with the same set of parameters.

  - Example:
    ```python
    audio_files = apiaudio.Speech.retrieve(scriptId="id-1234")
    ```

- `download()` Download the speech files in your preferred folder.

  - Parameters:

    - `scriptId` \* [Required] (string) - The script ID you want to download
    - `version` (string) - The version of the script to be downloaded. Default is "".
    - `section` (string) - The script section name you want to retrieve. If not provided, all the script sections will be returned.
    - `parameters` (dict) - Dict containing the personalisation parameters of your script. If not provided, the fallback track will be retrieved. This field depends on the parameters you used in your [script](#script)'s resource section. In order to retrieve a specific set of parameters, you need to create the speech with the same set of parameters.
    - `destination` (string) - The folder destination path. Default is "." (current folder)

  - Example:
    ```python
    audio_files = apiaudio.Speech.download(scriptId="id-1234", destination=".")
    ```

### `Voice` resource <a name = "voice"> </a>

Voice allows you to retrieve a list of the available voices from our API.

Voice methods are:

- `list()` List all the available voices in our API. The parameters are all optional, and can be used in combination to get the perfect voice for your usecase.

  - Parameters:
    - `provider` (string) - Try one of: google, polly, azure, msnr (aflorithmic), ibm, yandex, retro (aflorithmic), vocalid, resemble
    - `language` (string) - e.g. english, spanish, french, german, etc.
    - `accent` (string) - e.g. american, british, neutral, portuguese/brazilian, american soft, mexican, australian
    - `gender` (string) - Try with one of: male, female
    - `ageBracket` (string) - Try with one of: adult, child, senior
    - `tags` (string) - Try with one or more (separated by commas) of: steady, confident, balanced, informative, serious, instructional, slow, storytelling, calm, clear, deep, formal, sad, thin, fast, upbeat, fun, energetic, tense, very fast, flat, low pitched, high pitched, low-pitched, sing-y, cooperative, kind, stable, monotonous, neutral, responsible, business man, straight to the point, knowledgeable, focused, newscastery, newsreader, interviewer, reliable, friendly, welcoming, good for handing out information, slightly friendly
    - `industryExamples` (string) - Try with one or more (separated by commas) of: fitness, business, commercial, fashion, travel, audiobook, real estate, faith, health industry, comercial, realestate, kids entertainment, games, customer service, education, storytelling, entertainment, kids, education audiobook
    - `timePerformance` (string) - The time performance of the voice. There are three categories: slow, medium, fast.
    - `sectionCharacterLimit` (string) - The maximum amount of characters that the voice can process per Script section. All of the supported providers with the exception of VocalId have the limit of 4000.
  - Example:
    ```python
    all_voices = apiaudio.Voice.list()
    ```
  - Example:
    ```python
    french_voices = apiaudio.Voice.list(language="french",tags="steady, fun")
    ```

- `list_parameters()` This method lets you see which attributes you can filter the voices by, along with the allowed values for each attribute. You can later use these parameters and values to filter the voices you wish to list.

  - Parameters:

    - No parameters required.

  - Example:
    ```python
    parameters = apiaudio.Voice.list_parameters()
    ```

### `Sound` resource <a name = "sound"> </a>

Sound allows you to design your own sound template from a script and a background track. In order to get a sound template/project, make sure you requested [speech](#speech) for your script resource first.

Sound methods are:

- `list()` List all the available sound templates in our api. The parameters are all optional, and can be used in combination to get the perfect sound for your usecase.

  - Parameters:
    - `industryExamples` (string) - Try with one or more (separated by commas) of: news, travel, business, relaxation, fitness, relax, children stories
    - `contents` (string) - Try with one or more (separated by commas) of: intro, main, outro, effect1, effect2, main outro, droid_main, chewie_main, effect3, ambience, only effects
    - `genre` (string) - Try with one of: electronic, acoustic, atmospheric, abstract, rock
    - `tempo` (string) - Try with one of: mid, up, down, uptempo
    - `tags` (string) - Try with one or more (separated by commas) of: intense, minimal, reflective, melodic, happy, nostalgic, focus, energetic, uplifting, active, relaxed, ambience, mysterious, positive, informative, workout, work, meditation, travel, full silence
  - Example:
    ```python
    sound_templates = apiaudio.Sound.list()
    ```

- `list_parameters()` This method lets you see which attributes you can filter the sound templates by, along with the allowed values for each attribute. You can later use these parameters and values to filter the sound templates you wish to list.

  - Parameters:

    - No parameters required.

  - Example:
    ```python
    parameters = apiaudio.Sound.list_parameters()
    ```

### `Mastering` resource <a name = "mastering"> </a>

Mastering allows you to create and retrieve a mastered audio file of your script. A mastered version contains the speech of the script, a background track, personalised parameters for your audience and a mastering process to enhance the audio quality of the whole track. In order to get a mastered audio file, make sure you requested [speech](#speech) for your script resource first.

Mastering methods are:

- `create()` Create a mastered version of your script and choose the audio format.

  - Parameters:

    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `version` (string) - The version of the script to be produced. Default is "".
    - `soundTemplate` (string) - The sound template name. For the list of available sound templates check `apiaudio.Sound.list_sound_templates()` call.
    - `public` (boolean) - Boolean flag that allows to store the mastered file in a public s3 folder. Default value is `False`. Warning - This will cause your mastered files to be public to anyone in the internet. Use this at your own risk.
    - `vast` (boolean) - Boolean flag that allows to create a VAST file of your mastered file. The `vast` flag only works if `public` is `True`. Default value is `False`.
    - `endFormat` (list) - List of audio formats to be produced. Valid formats are: `["wav", "mp3" (default), "flac", "ogg", "mp3_very_low", "mp3_low", "mp3_medium", "mp3_high", "mp3_very_high", "mp3_alexa"]`
    - `forceLength` (int) - force the audio length of the mastered track (in seconds).
    - `audience` (dict) - Dictionary containing the personalisation parameters. This parameter depends on the number of parameters you used in your [script](#script) resource. In the script documentation example above, we used 2 parameters: `username` and `location`, and in the following example below we want to produce the script for username `salih` with location `Barcelona`. If audience is not provided, the fallback track will be created.
    - `mediaFiles` (list) - List of dicts containing the media files. This parameter depends on the media file tags used in the [script](#script) resource and the media files you have in your account. For example, if the script contains `<<media::myrecording>>` plus `<<media::mysong>>`, and you want to attach myrecording to mediaId = "12345", and mysong to mediaId = "67890" then `mediaFiles = [{"myrecording":"12345", "mysong":"67890"}]`.
    - `mediaVolumeTrim` (float) - Floating point varible that allows you to trim the volume of uploaded media files (in dB). This attribute has a valid range of -12 to 12 dB and applies to all media files included in a single mastering call. Clipping protection is not provided so only make incremental adjustments.
    - `connectors` (list) - List of dicts specifying configuration for particular 3rd party connection. For guidelines in context of supported 3rd party application, see [connectors documentation](https://docs.api.audio/docs/what-are-connectors).
    - `masteringPreset` (string) - The mastering preset to use, this enables features such as sidechain compression 'i.e. ducking' See `apiaudio.Mastering.list_presets()` for a list of presets and their descriptions.
    - `share` (boolean) - If you would like to have a sharable link created with your audio file, use this flag. If you put `share: True` the response will have `shareUrl` parameter returned. (Note: If you put this flag, your private files will be converted to public files.)

  - Example:
    ```python
    response = apiaudio.Mastering.create(
        scriptId="id-1234",
        soundTemplate="jakarta",
        audience={"username":"salih", "location":"barcelona"}
    )
    ```

- `create_media_timeline()` Creates a mastering request based purely on uploaded media files. Media files will need to be uploaded before calling this function. See [media](#media).

  - Parameters:

    - `timeline` \* [Required] (list) - The timeline object. A timeline object is a list of dictionaries, whereby each represents a track of audio files. Each track must have the following two keys `files` and `contentType`. 
      - `files` \* [Required] (list) Files is a list of dictionaries, whereby each entry must have the following 3 keys, `mediaId`, `startAt` and `endAt`
        - `files` \* [Required] (str) the mediaId of the file that has been uploaded.
        - `startAt` \* [Required] (float) the time that this media file should start at in seconds.
        - `endAt` \* [Required] (float) the time that this media file should end at in seconds.
        
       - `contentType` \* [Required] (string) - The type of content that this track contains, should be either `sound` or `speech`
    
    - `endFormat` (list) - List of audio formats to be produced. Valid formats are: `["wav", "mp3" (default), "flac", "ogg", "mp3_very_low", "mp3_low", "mp3_medium", "mp3_high", "mp3_very_high", "mp3_alexa"]`
    
    - `masteringPreset` (string) - The mastering preset to use, this enables features such as sidechain compression 'i.e. ducking' See `apiaudio.Mastering.list_presets()` for a list of presets and their descriptions.
    
  - Example:
    ```python

    backgroundId = apiaudio.Media.upload(file_path="background.wav")["mediaId"]
    speechId = apiaudio.Media.upload(file_path="speech1.wav")["mediaId"]

    timeline = [
      {
          "files" : [
              {
                  "mediaId" : speechId,
                  "startAt" : 2,
                  "endAt" : 14,
              }
          ],
          "contentType" : "speech"
      },
      {

          "files" : [
              {
                  "mediaId" : backgroundId,
                  "startAt" : 0,
                  "endAt" : 45,
              }
          ],
          "contentType" : "sound"
      }
    ]
    response = apiaudio.Mastering.create_media_timeline(timeline=timeline, masteringPreset="lightducking")

    ```

- `retrieve()` Retrieves the mastered file urls.

  - Parameters:

    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `versions` (string) - The version of the script to be retrieved. Default is "".
    - `parameters` (dict) - Dictionary containing the audience item you want to retrieve. If parameters are not provided, the fallback track will be retrieved.
    - `public` (boolean) - Boolean flag that allows to retrieve the mastered file from the public bucket. Use this if you want to retrieve a mastered file created using `public=True`. Default value is `False`.
    - `vast` (boolean) - Boolean flag that allows to retrieve the VAST file of your mastered file. The `vast` flag only works if `public` is `True`. Default value is `False`.
    - `endFormat` (list) - List of audio formats to be retrieved. Valid formats are:`["wav", "mp3" (default), "flac", "ogg", "mp3_very_low", "mp3_low", "mp3_medium", "mp3_high", "mp3_very_high", "mp3_alexa"]`

  - Example:
    ```python
    mastered_files = apiaudio.Mastering.retrieve(
      scriptId="id-1234",
      parameters={"username":"salih", "location":"barcelona"}
    )
    ```

- `download()` Download the mastered files in your preferred folder.

  - Parameters:
    - `scriptId` \* [Required] (string) - The [script](#script) resource ID.
    - `version` (string) - The version of the script to be downloaded. Default is "".
    - `parameters` (dict) - Dictionary containing the audience item you want to retrieve. If parameters are not provided, the fallback track will be downloaded.
    - `destination` (string) - The folder destination path. Default is "." (current folder)
    - `public` (boolean) - Boolean flag that allows to retrieve the mastered file from the public bucket. Use this if you want to retrieve a mastered file created using `public=True`. Default value is `False`.
    - `vast` (boolean) - Boolean flag that allows to retrieve the VAST file of your mastered file. The `vast` flag only works if `public` is `True`. Default value is `False`.
  - Example:
    ```python
    mastered_files = apiaudio.Mastering.download(
      scriptId="id-1234",
      parameters={"username":"salih", "location":"barcelona"}
      destination="."
    )
    ```
  - `list_presets()` List the available mastering presets.

    - Parameters:
      - No parameters required.

  - Example:

    ```python
    presets = apiaudio.Mastering.list_presets()
    print(presets)
    ```

### `Media` resource <a name = "media"> </a>

Media allows you to retrieve all the files available in api.audio for your organization.

Media methods are:

- `upload()` - Upload files to our databases.

  - Parameters:

    - `file_path` \* [Required] (string) - Relative path to the audio file.
    - `tags` (string) - Comma separated tags you want to add to your uploaded file. This will make retrieval easier.

  - Example:
    ```python
    apiaudio.Media.upload(
      file_path="./my_file.mp3",
      tags="tag1,tag2,tag3"
    )
    ```

- `list()` - List all files within an org.

  - Parameters:

    - `mediaId` (string) - If passed, will only return that file, or an empty object if it does not exist.
    - `tags` (string) - Comma separated tags you want to add to your uploaded file. If passed, will return all files that at least contain those tags.
    - `downloadUrl` (boolean): if True, a presigned url is added to each item on the array. This is slow for large amount of files (around 1s each).
    - `public` (boolean): If True, the media files listed will be the public media files provided by api.audio. Default is False.

  - Examples:

    ```python
    # lists all files
    files = apiaudio.Media.list()

    # lists files with tag="tag1"
    files = apiaudio.Media.list(tags="tag1")

    # lists file with specific id
    files = apiaudio.Media.list(mediaId="some_mediaId")

    # lists files with tag="tag1" and with a downloadurl
    files = apiaudio.Media.list(tags="tag1", downloadUrl=True)
    ```

- `list_tags()` This returns a list with all unique user defined tags.

  - Parameters:
    - No parameters required.

- Example:

  ```python
  tags = apiaudio.Media.list_tags()
  print(tags)
  ```

- `get_download_url()` - This method returns a presigned url for downloading a specific audio file
  - params:
    - `mediaId` \* [required] (string): media id for the file to be downloaded
- Example
  ```python
  url = apiaudio.Media.get_download_url(mediaId="some-mediaId")
  print(url)
  ```
- `download()` - This method downloads a specific audio file

  - params:
    - `mediaId` \* [required] (string): media id for the file to be downloaded
    - `destination` (string): path to the directory where the file will be downloaded. Default is "."

- Example
  ```python
  apiaudio.Media.download(
    mediaId="some_mediaId",
    destination="/my_destination_folder"
  )
  ```

### `SyncTTS` resource <a name = "synctts"> </a>

SyncTTS allows you to do Synchronous Text-To-Speech (TTS) with our API using all the voices available. Use it to create a speech audio file from a text and a voice name. The response contains wave bytes ready to be played or written to a file.

SyncTTS methods are:

- `create()` Create a TTS speech file.

  - Parameters:

    - `voice` \* [Required] (string) - The voice name. See the list of available voices using [Voice resource](#voice).
    - `text` \* [Required] (string) - The text you want to do TTS with. The limit is 800 characters for wave files.
    - `metadata` [Optional] ("full" or "none") - The level of metadata you want. Returns phoneme lists (only available for some msnr voices)

  - Example:
    ```python
    sync_tts = apiaudio.SyncTTS.create(
      voice="joanna",
      text="This is me creating synchronous text to speech",
      metadata="full"
    )
    ```

### `Birdcache` resource <a name = "birdcache"> </a>

Birdcache is a caching service provided by API.audio that provides the caching layer for the customer by storing data in API.audio servers for future use. This allows you to retrieve your speech files on the fly.

Birdcache methods are:

- `create()` Create a TTS speech file.

  - Parameters:

    - `type` \* [Required] (string) - Type of the event. Supported types are `mastering` and `speech`.
    - `text` \* [Required] (string) - The text you want to do speech/mastering with. See the example for personalisation parameters.
    - `voice` \* [Required] (string) - The voice for speech creation.
    - `audience` \* [Optional] (dict) - The key pair object for personalisation parameters. See the example below.
    - `soundTemplate` [Optional] (string) - The sound template for mastering creation. Only needed when the type is mastering.

  - Example:
    ```python
    birdcache = apiaudio.Birdcache.create(
      type="mastering",
      voice="linda",
      text="This is {{username|me}} creating synchronous text to speech",
      audience={"username": ["salih", "sam", "timo"]},
      soundTemplate="electronic"
    )
    ```

### `Pronunciation Dictionary` resource <a name = "pronunciationdictionary"> </a>

Often when working with TTS, the models can fail to accurately pronounce specific words, for example brands, names and locations are commonly mis-pronounced. As a first attempt to fix this we have introduced our lexi flag, which works in a similar way to SSML. For example, adding <!peadar> instead of Peadar (who is one of our founders) to your script will cause the model to produce an alternative pronunciation of this name. This is particularly useful in cases where words can have multiple pronunciations, for example the cities ‘reading’ and ‘nice’. In this instance placing <!reading> and <!nice> will ensure that these are pronounced correctly, given the script:

`" The city of <!nice> is a really nice place in the south of france."`

If this solution does not work for you, you can instead make use of our custom (self-serve) lexi feature.

This can be used to achieve one of two things, correcting single words, or expanding acronyms. For example, you can replace all occurrences of the word Aflorithmic with “af low rhythmic” or occurrences of the word ‘BMW’ with “Bayerische Motoren Werke”. Replacement words can be supplied as plain text or an IPA phonemisation.

Prononciation dictionary methods are:

- `list()` Lists the publicly available dictionaries and their words

  - Parameters:

    - `none`

  - Example:

    ```python
    # returns a list of public dictionaries
    dictionaries = apiaudio.Lexi.list()

    ```

- `list_custom_dicts()` Lists the custom dictionaries and their respective words

  - Parameters:
    - `none`
  - Example:

    ```python
    # returns a list of custom dictionaries
    types = apiaudio.Lexi.list_custom_dicts()

    ```

- `register_custom_word` Adds a new word to a custom dictionary.

  - `lang` [required] (string) - Language family, e.g. `en` or `es`.dictionary - use `global` to register a word globally.
  - `word` [required] (string) - The word that will be replaced
  - `replacement` [required] (string) - The replacement token. Can be either a plain string or a IPA token.
  - `contentType` [optional] (string) - The content type of the supplied replacement, can be either `basic` (default) or `ipa` for phonetic replacements.
  - `specialization` [optional] (string) - by default the supplied replacement will apply regardless of the supplied voice, language code or provider. However edge cases can be supplied, these can be either a valid; provider name, language code (i.e. en-gb) or voice name.
  -
  - Example:
    ```python
      # correct the word sapiens
      r = apiaudio.Lexi.register_custom_word(word="sapiens", replacement="saypeeoons", lang="en")
      print(r)
    ```

  For each language, only a single word entry is permitted. However, each word can have multiple `specializations`. When a word is first registered a `default` `specialization` is always created, which will match what is passed in. Subsequent calls with different specializations will only update the given specialization. The exact repacement that will be used is determined by the following order of preference:

  ` voice name > language dialect > provider name > default`

  For example, a replacement specified for voice name `sara` will be picked over a replacement specified for provider `azure`.

- `list_custom_words()` Lists all the words contained in a custom dictionary.

  - Parameters:

  - `lang` [required] (string) - Language family, e.g. `en` or `es` - use `global` to list language agnostic words.
  - Example:
    ```python
    # lists all words in the dictionary along with their replacements
    words = apiaudio.Lexi.list_custom_words(lang="en")
    ```

#### Preview

The effect of applying the Pronunciation Dictionary can be seen with the `script.preview()` method. See [Script](#script) documentation for more details.

- Example:

  ```python
    text = """
      The author of this repo has lived in two places in the
      UK, <!Bude> and <!Bristol>
    """

  r = apiaudio.Script.create(scriptText=text)
  scriptId = r["scriptId"]

  # preview the script in en-gb
  preview = apiaudio.Script.preview(scriptId=scriptId, voice="Joanna")
  print(preview)
  ```

- Response:
  ```python
  {"preview" : "The author of this repo has lived in two places in the UK, bude and <phoneme alphabet=\"ipa\" ph=\"###\"> bristol </phoneme>"}
  ```
  In this example `Bristol` will be phonemised to ensure it is correctly pronouced, but as `Bude` is not in our a dictionaires it is left as is. The exact IPA tokens for words in our internal dictionaires are obsfucated.

### `Connector` resource <a name = "connector"> </a>

Resource used for monitoring 3rd paty integrations. End results of [Mastering](#mastering) resource can be distributed into external applications through `connectors` field. See [connectors documentation](https://docs.api.audio/docs/what-are-connectors).
List of currently supported applications:

- [julep.de](https://www.julep.de)

Available methods:

- `retrieve()` After registering a connector in the [api.console](https://console.api.audio/), use this method to check whether a connection was succesful using provided credentials.

  - Parameters:

    - `name` \* [Required] (string) - The name of the connector specified in console.

  - Example:
    ```python
    status = apiaudio.Connector.retrieve(
      name="julep"
    )
    ```

- `connection()` Check the status of the connection by providing `connectionId` returned in a Mastering response.

  - Parameters:

    - `connection_id` \* [Required] (string) - The connectionId returned by Mastering resource.

  - Example:
    ```python
    status = apiaudio.Connector.connection(
      connection_id="af2fe14a-aa6b-4a97-b430-a072c38b11ff"
    )
    ```

### `Orchestrator` resource <a name = "Orchestrator"> </a>

The orchestrator is used to make working with a range of audio services as easy as sending a single API request. Each route here is carefully configured to produce high-quality and easy to access audio assets.

Orchestrator methods are:

- `create_audio()` Creates a simple TTS speech request and adds a sound template to it through mastering.

  - Parameters:

    - `scriptText` \* [Required] (str) - Text to synthesize (TTS).
    - `soundTemplate` (str) - Sound template to use.
    - `voice` \* [Required] (str) - Name of voice to use.

- `create_three_sections()` Creates a TTS speech request with 3 sections and adds a sound template to it through mastering.

  - Parameters:

    - `introText` \* [Required] (str) - Text to synthesize in the intro section.
    - `mainText` \* [Required] (str) - Text to synthesize in the main section.
    - `outroText` \* [Required] (str) - Text to synthesize in the outro section.
    - `soundTemplate` (str) - Sound template to use.
    - `voice` \* [Required] (str) - Name of voice to use.

- `media_with_sound()` Combines a pre-existing media file (i.e. pre-recorded voice) with a sound template

  - Parameters:

    - `mediaId` \* [Required] (str) - MediaId of the media file to use as input.
    - `soundTemplate` \* [Required] (str) - Sound template to use.

### Webhooks

This SDK provides an easy way of verifying apiaudio webhook call security headers. It is highly recommended for you to verify the headers in order to protect your server from any malicious attack.

The method is:

```python
apiaudio.Webhooks.verify(payload, sig_header, secret, tolerance)
```

It will return true if the header is valid, otherwise it will raise an error.
The parameters to pass are; `payload` being the body object sent by apiaudio, `sig_header` being `X-Aflr-Secret` in the request headers sent by apiaudio, `secret` being your webhook secret (you can get it in apiaudio console) and `tolerance` being the tolerance in seconds for the header checks, which defaults to 300 seconds.

### Logging <a name = "logging"></a>

By default, warnings issued by the API are logged in the console output. Additionally, some behaviors are logged on the informational level (e.g. "In progress..." indicators during longer processing times).
The level of logging can be controlled by choosing from the standard levels in Python's `logging` library.

- Decreasing logging level for more detailed logs:
  ```python
  apiaudio.set_logger_level("INFO")
  # apiaudio.set_logger_level("CRITICAL") - set the highest level to disable logs
  ```

# Maintainers <a name = "maintainers"> </a>

- https://github.com/Sjhunt93
- https://github.com/martinezpl

# Development

There is a pre-commit hook that will run before you commit a file. This is to keep the code standards high. To enable it, you should run `make`. Then it will set up the pre-commit hook for git. Thats all! Now every time before you commit, it will run to tell you about the standards.

If you use VSCode for committing files, you may bump into `pre-commit command not found` error. That is ok, just run `brew install pre-commit` or your fave package manager [from the list here](https://pre-commit.com/#installation).

If you bump into `your pip version is old` error, just ignore it and use the terminal.

If there is a problem and you are in a rush, you can add `--no-verify` at the end of the commit command, it will skip the pre-commit hooks, e.g `git commit -m 'your commit message' --no-verify`

# License <a name = "license"> </a>

This project is licensed under the terms of the MIT license.
