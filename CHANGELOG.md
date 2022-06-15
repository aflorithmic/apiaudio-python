# Changelog

- Friday \*\* June 2022
  v0.16.2

## Enhancements

- We introduced a new function called `set_assume_org_id` for incoming super organization feature. By using this method, you can assume the id of a child organization as their super organization, and make your calls on behalf of them.

A super organization is loosely modelled on superuser. So you can as a company ACME have specific criteria and permissions - and then you can share these with your child organisations. This allows you fine grained 

- Friday 20th May 2022
  v0.16.1

## Bug fixing

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

## New released features

- Enhancements of voices. We've been testing with some users a more natural pauses to our custom voices. We contacted customers affected and some requested to not have this feature enabled please contact us if you want to use the old voices. We do feel that these voices are more natural and our beta testing was positive. These will be available soon under `msnr` voices in our API.

- As a developer user I want to share my audio with my team/bosses/business person so they can try and test the wonders of api.audio. We call this _virality link_ and it's available in the console soon.

- Friday 13th May 2022

v0.16.0

## Features

- We added new endFormat (for making sure your audio is the correct format for a target audience) this week we added Alexa preset

```python
 m = apiaudio.Mastering().create(scriptId=GLOBAL_SCRIPT_ID, endFormat="mp3_alexa")
```

In the future we will add other endFormats - please tell us which ones you'd like.

- To continue to be able to offer free content to those of you still getting to know API.audio, we have added a watermark to our files.

### Corporate features

- For our corporate plan users we've enabled `sandboxing` this allows you to test safely API requests without using up credits. Please contact your account manager for further details.

## Breaking Changes

- Our feature (pronunciation dictionary) has had some usability enhancements. The biggest change is adding `useDictionary` as a boolean.
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

- Enhancements of voices. We've been testing with some users a more natural pauses to our custom voices. We contacted customers affected and some requested to not have this feature enabled please contact us if you want to use the old voices. We do feel that these voices are more natural and our beta testing was positive. These will be available soon under `msnr` voices in our API.

- As a developer user I want to share my audio with my team/bosses/business person so they can try and test the wonders of api.audio. We call this _virality link_ and it's available in the console soon.

- We've been developing the usability of our data capture app for voice cloning (this is available in some plans). You'll see this in the next few weeks.
