# Changelog

* Friday 13th May 2022

v0.6.0
## Features
* We added new endFormat (for making sure your audio is the correct format for a target audience) this week we added Alexa preset
```python
 m = apiaudio.Mastering().create(scriptId=GLOBAL_SCRIPT_ID, endFormat="mp3_alexa")
 ```
In the future we will add other endFormats - please tell us which ones you'd like.

* To continue to be able to offer free content to those of you still getting to know API.audio, we have added a watermark to our files.


### Corporate features
* For our corporate plan users we've enabled `sandboxing` this allows you to test safely API requests without using up credits. Please contact your account manager for further details.


## Breaking Changes
* Our feature (pronunciation dictionary) has had some usability enhancements. The biggest change is adding `useDictionary` as a boolean.
Here's an example
  ```python
  scriptText = """Hello I am reading a book in the city of <!location>reading<!> today"""
  script = apiaudio.Script.create(scriptText=scriptText)
  speech = apiaudio.Speech.create(scriptId=script["scriptId"], voice="Ryan", useDictionary=True)
  print(speech)
  ```
The addition of useDictionary and the change in behaviour is likely to present some breaking changes. We've notified any customers who are affected.

## Bug Fixing
We had some third party downtime with some voices from one provider. We notified them and fixed this issue.

## Maintenance
We have removed old code and streamlined other code using our Mastering engine. This will allow us to add features more easily whilst removing unnecessary complexity.
We also made various performance improvements and work in the background. Although not all of this will be customer facing, these incremental improvements are very important.

## Unreleased
(These are features that aren't added yet, but will be released next week)
* Enhancements of voices. We've been testing with some users a more natural pauses to our custom voices. We contacted customers affected and some requested to not have this feature enabled please contact us if you want to use the old voices. We do feel that these voices are more natural and our beta testing was positive. These will be available soon under `msnr` voices in our API.

* As a developer user I want to share my audio with my team/bosses/business person so they can try and test the wonders of api.audio. We call this *virality link* and it's available in the console soon.

* We've been developing the usability of our data capture app for voice cloning (this is available in some plans). You'll see this in the next few weeks.
