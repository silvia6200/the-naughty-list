from naughtylist.models import Voice
from TwitterAPI import TwitterAPI
from datetime import datetime
from django.utils import timezone
import re
import os

FILTER = 'naughtylist'
TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET = os.environ['TWITTER_API_SECRET']
TWITTER_ACCESS_TOKEN_KEY = os.environ['TWITTER_ACCESS_TOKEN_KEY']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


def parse_and_store_tweet(status):

    assert isinstance(status, dict)

    today = timezone.now()

    test_output = dict()
    valid = False
    company_name = ''
    reason = ''
    message = ''
    date = today


    hashtags = status.get('entities').get('hashtags')

    test_output['hashtagcount'] = len(hashtags)

    #check at least two hashtags exist
    if (len(hashtags) >= 2):

        #check naughtylist hashtag is at the start of the stream
        if (hashtags[0].get('text') == FILTER) and (hashtags[0].get('indices')[0] == 0):

            #check next hashtag appears straight after
            if hashtags[1].get('indices')[0] == (hashtags[0].get('indices')[1] + 1):
                #if it does, tweet is valid
                valid = True

                # set company name value
                company_name = hashtags[1].get('text')

                # set date value
                date = datetime.strptime(status.get('created_at'), '%a %b %d %H:%M:%S +0000 %Y')

                # set twitter user value
                user = status.get('user').get('screen_name')

                #check if reason hashtag appears straight after company hashtag
                if (hashtags[2].get('indices')[0]) == (hashtags[1].get('indices')[1] + 1):

                    #if yes, set reason and set rest of tweet as message...
                    reason = hashtags[2].get('text')
                    message = status.get('text')[(hashtags[2].get('indices')[1]+1):]

                else:
                    #if not, set all text after company name as message...
                    reason = ''
                    message = status.get('text')[(hashtags[1].get('indices')[1]+1):]

            #check if user has already published tweet on same day as given tweet
            existing_tweets_from_user = Voice.objects.filter(user=user,date_added=today.date())

            #if user has not already published a tweet today then store tweet
            if existing_tweets_from_user.count() == 0:
                voice = Voice(user=user,offender=company_name,reason=reason,message=message,naughty=True,fuzzy=True,datetime_added=date,date_added=date.date())
                voice.save()

    #return results for testing
    test_output = dict()
    test_output['valid'] = valid
    test_output['company_name'] = company_name
    test_output['reason'] = reason
    test_output['message'] = message
    test_output['date'] = date
    return test_output


def format_test_tweets(tweet,user,date):
    """
    :type tweet: str
    :type user: str
    :type date: datetime
    """
    assert isinstance(tweet, str)
    assert isinstance(user, str)
    assert isinstance(date, datetime)

    #find hashtags in tweet and format as list of tags and indices
    hashtags = [dict({'indices': [m.start(), m.end()], 'text': m.group(0).strip('#')}) for m in re.finditer(r'(#[0-9a-zA-Z]+)', tweet)]

    #create tweet structure based on TwitterAPI output
    output = dict()
    output['text'] = tweet
    output['entities'] = dict({'hashtags': hashtags})
    output['user'] = dict()
    output['user']['screen_name'] = user
    output['created_at'] = datetime.strftime(date,'%a %b %d %H:%M:%S +0000 %Y')
    return output


class TweetFetcher():
    def __init__(self):
        self.filter = '#' + FILTER

    def run(self):
        self.api = TwitterAPI(TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN_KEY, TWITTER_ACCESS_TOKEN_SECRET)
        self.r = self.api.request('statuses/filter', {'track':self.filter})
        for item in self.r.get_iterator():
            parse_and_store_tweet(item)

            print item

