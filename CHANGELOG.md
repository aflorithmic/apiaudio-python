# Changelog

## Friday 8th July 2022

### New Voices
* We added one of our Partners [Cereproc](www.cereproc.ai) you can see the voices here [Voices](https://library.api.audio/voices?providerFullName=cerevoice)
* You can try out a voice from Cereproc with this example
```python 
import apiaudio 
apiaudio.api_key="API-KEY"
script = apiaudio.Script.create(scriptText="<<soundSegment::intro>><<sectionName::intro>>Hello world. Welcome to API dot audio.<<soundSegment::main>><<sectionName::main>> Create audio in a few easy steps.")
response = apiaudio.Speech.create(scriptId=script.get("scriptId"), voice="dakota") 
response = apiaudio.Mastering.create(scriptId=script.get("scriptId"), soundTemplate = "parisianmorning" )
file = apiaudio.Mastering.download(scriptId=script.get("scriptId"))
```

### Console 
We've been updating the console a lot. 
You can see some images here of Get Started
![Get Started](images/console_screenshot_getstarted.png)
You can see the changelog here
![Changelog](images/console_screenshot_changelog.png)

### Voice cloner
* We shipped a new version of [voice cloner](https://voice-cloning.api.audio/capture)
* This is up to a 3X faster User Experience. 

### SuperOrg

* We improved superorg and integrated billing. So child orgs API consumption now contributes to your bill. And we added metering and analytics (you'll need to contact matt@aflorithmic.ai for that) 
![SuperOrg](images/console_screenshot_superorg.png)

* SDK support for superorgs and all assuming mechanism. Both for JS and Python sdks. [See the SDK here](https://github.com/aflorithmic/apiaudio-python#super-organizations)

### Billing
We've optimised our pricing for usage. 
* 250 free credits on sign up, instead of 500.
* Monthly allowance for free plans, instead of giving them time till the end of month regardless what day 
they signed up. This way, free organisations will have 28 days to use their credits. We will add some email 
marketing about this as well. 

## Friday 1st July 2022
### Voice cloner update
- UX improvements
- Bug free :) 
- Setup page
- Silence detector (hands free operation)
- AES version 2 - better UX for our customers (threshold adjustments) 

How can I get started? 
You'll be able to sign up with [https://voice-cloning.api.audio/](Voice-cloning)

### Webhooks
- We're delighted to ship a much requested feature from customers! *Webhooks*
- If you're looking for a good explanation of webhooks we recommend [this blog post](https://zapier.com/blog/what-are-webhooks/) but basically these are automated messages (akin to SMS) sent from APIs when something happens in an API. A common use case for us is mastering requests. Some mastering requests take some time to run, so you may want to simply set these up with webhooks and have a better customer experience :) 
You can see some image here
![First webhook image](images/webhook_screenshot_1_24th_june_2022.png)
You'll receive the logs of the webhooks here
![Second webhook image](images/webhook_screenshot_2_24th_june_2022.png)

Here's some code as well. Let's say you have a long running mastering request. It might take 30s. 
Rather than waiting for the request to run - you can simple add a callback url. 

```python 
apiaudio.Mastering().create(scriptId=script_id, callback_url='call-based callback url')
```

We also have some awesome security features such as verifying signatures. We'll add more to the docs about this soon. 
```python
apiaudio.Webhooks.verify(event_body, x-aflr-secret, clients_webhook_secret, tolerance = defaults to 300 seconds)
```
### Enhanced Watermarks
- Our free plan has watermarks, if you want these removed you'll have to upgrade. We've added these to multiple languages. 
Here are some examples
```shell 
WATER_MARKS = {
    "default" : ". Created with API audio.",
    "en" : ". Created with API audio.",
    "pl" : ". Stworzone przy użyciu API audio.",
    "ga" : ". Cruthaithe le fuaim API audio",
    "tr" : ". api.audio ile oluşturuldu",
    "fr" : ". créé avec API audio",
    "ca-es" : ". creat amb API audio",
    "ca" : ". creat amb API audio",
    "el" : ". Δημιουργήθηκε με το api.audio",
    "nl" : ". Gemaakt met API audio",
    "de" : ". Erstellt mit api punkt audio.",
    "pt-br" : ". Criado com api.audio",
    "pt" : ". Criado com api.audio",
    "hu" : ". Az api.audio felhasználásával készült.",
    "et" : ". valmistaja Api audio",
    "hi" : ". yeh aawaaz api audio se banayi gayi",
    "zh" : ". 用Api audio製作的",
    "ua" : "створено за допомогою API крапка аудіо",
    "bn" : "API অডিও দিয়ে তৈরি করা |"
}
```

### SuperOrgs added to the console
- We're going to add to the console the SuperOrg functionality enabling users to administer functionality for the companies that are using their accounts. 
- There's a lot more fine grained control coming as well, but this is an *enterprise ready* feature and requested by numerous customers. If you want a demo feel free to reach out.
![Mockup of SuperOrg](images/console_superorg_screenshot_1_1st_july_2022.png)

### Visemes 2.0
Online (sync) Visemes 2.0: We have onboarded all of our customers' feedback, and we are now confident to launch a new version, the result of 3 months of R&D. There are substantial improvements in alignment, speed and latency. They are deployed in our custom `msnr` voices

### Bug fixes
- Some customers reported that the amplitude of some of our `msnr` voices was louder on the 
second sentence and not the first sentence. We created a fix for this, and we hope this fixes the error. 

### Coming soon new partnerships
- We have new partnerships for our beta customers please reach out to us to learn more to try out new voices. 

## Friday 24th June 2022
v.0.16.3 
### SuperOrg
- Listing superorgs - the ability to list these organisations.
- Billing integration so each superorg and child org is charged correctly. 

### Voice Cloner
Our Data Capture App used as part of our voice cloning process is now rebranded *voice cloner* 

These are the top bug fixes this week which should result in a much better user experience
* Microphone not detected on some Mobile Phones. (Fixed)
* Play button not playing back full audio. (Fixed)
* “Record” button wasn’t recording full sentences. (Fixed)
* AutoGain was causing distorting in audio (Fixed)

You can try it out here [Voice Cloner](https://voice-cloning.api.audio/)


### Bug Fixes 
- We fixed a bug that was showing hidden voices in the voice library. This was hurting the user experience. 

### German Voice
- We've shipped the following to select Beta customers. If you want access let us know and we'll give you access. 
It's our best voice ever created by our internal TTS research team - it's called `margareta-v1`
```python
# script text
text = text = """
Hallo Peadar. Ich wurde am 20.06.2022 in der Softwareschmiede von Aflorithmic in Produktion eingesetzt.
"""
# script creation
script = apiaudio.Script.create(scriptText=text, scriptName="breaking_news")


r = apiaudio.Speech().create(
    scriptId=script.get("scriptId"),
    voice="margareta-v1",
    speed=110,
)

template = "breakingnews"
response = apiaudio.Mastering().create(
    scriptId=script.get("scriptId"),
    soundTemplate=template
)

print(response)

file = apiaudio.Mastering().download(
    scriptId=script.get("scriptId"), destination=".")
print(file)
```
You can listen to an example here <video src="https://user-images.githubusercontent.com/983944/175528852-84d5dc2e-3780-4642-9d87-fccb8facab48.mp4
"></video>

### Bug fixing
- We discovered an incorrect billing issue with some voices on our platform (only affecting IBM voices). This only impacted some customers all customers have been informed and refunded. We've added alarms and detection mechanisms and enhanced quality control to fix this going forward. We're sorry for any inconvenience. 
- We're implementing changes to handle this and working on our reliability and monitoring. 


### Console updates
We've been working hard on our console in the recent weeks. And you can view it [here](https://console.api.audio/)
You can see the easier view of Total api calls, Script api calls, Speech api calls and Mastering api calls
![First console image](images/console_screenshot_1_24th_june_2022.png)
If you click on these you'll see some other information including this *awesome* donut chart
![Second console image](images/console_screenshot_2_24th_june_2022.png)
And if you want to dive deep into this have a look here at the logs
![Third console image](images/console_screenshot_3_24th_june_2022.png)

These are just some highlights of the stuff we've improved based on customer feedback :) 
## Friday 17th June 2022
  v0.16.2

### Enhancements

- We introduced a new function called `set_assume_org_id` for incoming super organization feature. By using this method, you can assume the id of a child organization as their super organization, and make your calls on behalf of them.

A super organization is loosely modelled on superuser. So you can as a company ACME have specific criteria and permissions - and then you can share these with your child organisations. This allows you fine grained control of users and their roles and permissions and the ability to share settings and voices across orgs. We were informed by IAM from AWS in our design. If you want access let us know, we're working hard on this. This is part of a whole 

- *Voices* We have some great partnerships coming up with 2 new voice providers. Reach out to us if you want to know more :) 
### Coming soon 
Under msnr we will soon have another german voice. We're testing this with some beta customers the `margareta-v1` voice. 
(Updated above)


We've also improved our performance and invested more in 

## Friday 20th May 2022
  v0.16.1

### Bug fixing

- We noticed in testing some additional latency caused by our feature flag implementation - so we refactored this to make it much faster. This was mostly visible in our custom voice implementations.

### Enhancements

- We added the ability to share audio with other users. It's a magic link feature.
  For example

```shell
curl -X POST \
  'https://v1.api.audio/mastering' \
  --header 'x-api-key: API-KEY' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "scriptId": "xx",
    "share": true
}'
```

This returns a url - if you goto

https://console-api.audio/share?id=your_id

You'll get a page that you can share with your organisation and via Whatsapp and other social
networks.

- We've updated our [voice library page](https://library.api.audio/voices) to have faster loading and we've added some other improvements in the GET request for voices so you can have a better voice discovery experience. Most of this is backend and performance enhancements.
- Enhanced query parameters for voice discoverability

`GET https://v1.api.audio/voice?tags=upbeat,storytelling`

Will voices that have both of these tags. We also introduced pagination as well.

**Pagination**
(Not yet available in the SDK)
Use parameter `limit` to set the amount of returned voices. Use `offset` to iterate through the results.

E.g.

`GET https://v1.api.audio/voice?limit=10&offset=10`

`GET https://v1.api.audio/voice?limit=10&offset=20`

`GET https://v1.api.audio/voice?limit=10&offset=30`

**Query body in POST /voice**

A `query` JSON is available in POST method.

**Supported operators:**

> `"$gt", "$gte", "$lt", "$lte", "$contains", "$is_in", "$ne"`

**Basic query (attribute equals x):**

```json
{
  "query": {
    "language": "english",
    "provider": "polly"
  }
}
```

**List specific languages:**

```json
{
  "query": {
    "language": {
      "$is_in": ["english", "spanish", "polish"]
    }
  }
}
```

**List only private and public_paid tiers:**

```json
{
  "query": {
    "tier": {
      "$ne": "public"
    }
  }
}
```

**List spanish voices where priority is less than or equal to 3:**

```json
{
  "query": {
    "language": "spanish",
    "priority": { "$lte": 3 }
  }
}
```

There's a lot you can do with this so we hope this makes your develper experience easier.

### New released features

- Enhancements of voices. We've been testing with some users a more natural pauses to our custom voices. We contacted customers affected and some requested to not have this feature enabled please contact us if you want to use the old voices. We do feel that these voices are more natural and our beta testing was positive. These will be available soon under `msnr` voices in our API.

- As a developer user I want to share my audio with my team/bosses/business person so they can try and test the wonders of api.audio. We call this _virality link_ and it's available in the console soon.

## Friday 13th May 2022

v0.16.0

### Features

- We added new endFormat (for making sure your audio is the correct format for a target audience) this week we added Alexa preset

```python
 m = apiaudio.Mastering().create(scriptId=GLOBAL_SCRIPT_ID, endFormat="mp3_alexa")
```

In the future we will add other endFormats - please tell us which ones you'd like.

- To continue to be able to offer free content to those of you still getting to know API.audio, we have added a watermark to our files.

### Corporate features

- For our corporate plan users we've enabled `sandboxing` this allows you to test safely API requests without using up credits. Please contact your account manager for further details.

### Breaking Changes

- Our feature (pronunciation dictionary) has had some usability enhancements. The biggest change is adding `useDictionary` as a boolean.
  Here's an example
  ```python
  scriptText = """Hello I am reading a book in the city of <!location>reading<!> today"""
  script = apiaudio.Script.create(scriptText=scriptText)
  speech = apiaudio.Speech.create(scriptId=script["scriptId"], voice="Ryan", useDictionary=True)
  print(speech)
  ```
  The addition of useDictionary and the change in behaviour is likely to present some breaking changes. We've notified any customers who are affected.

### Bug Fixing

We had some third party downtime with some voices from one provider. We notified them and fixed this issue.

### Maintenance

We have removed old code and streamlined other code using our Mastering engine. This will allow us to add features more easily whilst removing unnecessary complexity.
We also made various performance improvements and work in the background. Although not all of this will be customer facing, these incremental improvements are very important.

### Unreleased

(These are features that aren't added yet, but will be released next week)

- Enhancements of voices. We've been testing with some users a more natural pauses to our custom voices. We contacted customers affected and some requested to not have this feature enabled please contact us if you want to use the old voices. We do feel that these voices are more natural and our beta testing was positive. These will be available soon under `msnr` voices in our API.

- As a developer user I want to share my audio with my team/bosses/business person so they can try and test the wonders of api.audio. We call this _virality link_ and it's available in the console soon.

- We've been developing the usability of our data capture app for voice cloning (this is available in some plans). You'll see this in the next few weeks.
