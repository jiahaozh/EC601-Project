import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from aylienapiclient import textapi

def fetch_new_stories(params={}):
  fetched_stories = []
  stories = None

  while stories is None or len(stories) > 0:
    try:
      response = api_instance.list_stories(**params)
    except ApiException as e:
      #if ( e.status == 429 ):
        print('Usage limit are exceeded. Wating for 60 seconds...')
        #time.sleep(60)
        continue

    stories = response.stories
    params['cursor'] = response.next_page_cursor

    fetched_stories += stories
    print("Fetched %d stories. Total story count so far: %d" %
      (len(stories), len(fetched_stories)))

  return fetched_stories
# Text API client initialization
textclient = textapi.Client('ca1bf90f','b90fbda94f7178ec1c561bb3f1a4023c')
# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'de624fbc'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '74607d61d5a4856236987e6cc4197bf0'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

params = {
  'title': 'Apple',
  'language': ['en'],
  'published_at_start': 'NOW-2DAY',
  'published_at_end': 'NOW-43HOUR',
  #'categories_taxonomy': 'iab-qag',
  #'categories_id': ['IAB17'],
  'cursor': '*',
  'per_page': 10
}

stories = fetch_new_stories(params)

for story in stories:
    #print(story.title + " / " + story.source.name)
    #print (story.published_at)
    #print (story.sentiment)
    senti=textclient.Sentiment(story.body)
    print(senti['polarity'], senti['polarity_confidence'])
    #print(senti['subjectivity'], senti['subjectivity_confidence'])

print('************')
print("Fetched %d stories which are in English, are \
about Sports and were published between %s and %s" %
(len(stories), params['published_at_start'], params['published_at_end']))
