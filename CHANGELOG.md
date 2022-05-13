# Changelog

* Friday 13th May 2022

`Users needs are our strategy and our tactics` 
v0.6.0
## Features
* We added new endFormat (for making sure your audio is the correct format for a target audience) this week we added Alexa preset 
```python
 m = apiaudio.Mastering().create(scriptId=GLOBAL_SCRIPT_ID, endFormat="mp3_alexa")```

* As a developer user I want to share my audio with my team/bosses/business person so they can try and test the wonders of api.audio. We call this *virality link* and it's available in the console now. 

## Enterprise features
* For our enterprise users we've enabled `sandboxing` this allows you to test safely API requests without using up credits. Please contact your account manager for further details. 

## Enhancements
* Improved pronunciation of our custom voices. We had some pronunctuation issues reported by customers, this adds more natural sounding pauses to our voices.

## BreakingChanges
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
Maintenance
We removed old code and streamlined some code with our Mastering engine. This will help us add features more easily and remove unnecessary complexity. 
We also did various performance improvements and work in the background, not much of this will be customer facing but incremental improvements are important. 
