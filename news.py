from aylienapiclient import textapi
import aylien_news_api
from aylien_news_api.rest import ApiException

# Text API client initialization
textclient = textapi.Client('ca1bf90f','b90fbda94f7178ec1c561bb3f1a4023c')
# Configure API key authorization: app_id
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = 'de624fbc'
# Configure API key authorization: app_key
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '74607d61d5a4856236987e6cc4197bf0'
# create an instance of the API class
newsclient = aylien_news_api.DefaultApi()

'''
text = 'This is extremely bad'
sentiment = textclient.Sentiment(text)
print (sentiment)
'''
opts = {
        'title': 'Apple',
        #'body': 'Iphone',
        #'sort_by': 'social_shares_count.facebook',
        'language': ['en'],
        'not_language': ['es', 'it'],
        'published_at_start': 'NOW-1YEAR',
        'published_at_end': 'NOW',
        'per_page': 100,
        #'cursor': '*',
        'next_page_cursor': 10
        #'entities_body_links_dbpedia': [
        #'http://dbpedia.org/resource/Donald_Trump',
        #'http://dbpedia.org/resource/Hillary_Rodham_Clinton'
        #]
}
try:
        # List stories
        api_response = newsclient.list_stories(**opts)
        #api_response = api_instance.list_stories(**opts)
        print("API called successfully. Returned data: ")
        print("========================================")

        aaa = len(api_response.stories)
        print(aaa)

        for story in api_response.stories:
            #print(story.title + " / " + story.source.name)
            print (story.published_at)
            #print (story.sentiment)
            senti=textclient.Sentiment(story.body)
            print(senti['polarity'], senti['polarity_confidence'])
            #print(senti['subjectivity'], senti['subjectivity_confidence'])

except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %s\n" % e)
