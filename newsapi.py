import time
import aylien_news_api
from aylien_news_api.rest import ApiException

def fetch_new_stories(params={}):
  fetched_stories = []
  stories = None

  while stories is None or len(stories) > 0:
    try:
      response = api_instance.list_stories(**params)
    except ApiException as e:
      if ( e.status == 429 ):
        print('Usage limit are exceeded. Wating for 60 seconds...')
        time.sleep(60)
        continue

    stories = response.stories
    params['cursor'] = response.next_page_cursor

    fetched_stories += stories
    print("Fetched %d stories. Total story count so far: %d" %
      (len(stories), len(fetched_stories)))

  return fetched_stories

# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'de624fbc'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '74607d61d5a4856236987e6cc4197bf0'

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()

params = {
  'language': ['en'],
  'published_at_start': 'NOW-10HOUR',
  'published_at_end': 'NOW',
  'categories_taxonomy': 'iab-qag',
  'categories_id': ['IAB17'],
  'cursor': '*',
  'per_page': 16
}

stories = fetch_new_stories(params)

print('************')
print("Fetched %d stories which are in English, are \
about Sports and were published between %s and %s" %
(len(stories), params['published_at_start'], params['published_at_end']))
