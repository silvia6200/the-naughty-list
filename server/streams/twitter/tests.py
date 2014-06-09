from django.test import TestCase
from django.utils import timezone
from datetime import datetime

from streams.twitter.tweetparser import format_test_tweets, parse_and_store_tweet
from naughtylist.models import Voice

DT = timezone.now()
tweet1 = format_test_tweets('#naughtylist','whistleblower',DT)
tweet2 = format_test_tweets('#naughtylist #companyname #reason this company is bad','whistleblower',DT)
tweet3 = format_test_tweets('#naughtylist #companyname #reason this company is bad','goodguy',DT)


class TestTweetFormatterTests(TestCase):

    def test_tweet1(self):

        expected = {'text': '#naughtylist',
                     'entities':
                         {
                             'hashtags':
                                 [{'indices': [0, 12], 'text': 'naughtylist'}],
                             },
                     'user': {'screen_name': 'whistleblower',},
                     'created_at': datetime.strftime(DT,'%a %b %d %H:%M:%S +0000 %Y'),
                     }
        self.assertEqual(tweet1,expected)

    def test_tweet2(self):
        self.maxDiff = None
        expected = {'text': '#naughtylist #companyname #reason this company is bad',
                     'entities':
                         {
                             'hashtags':
                                 [
                                     {'indices': [0, 12], 'text': 'naughtylist'},
                                     {'indices': [13, 25], 'text': 'companyname'},
                                     {'indices': [26, 33], 'text': 'reason'}
                                 ],

                             },
                     'user': {'screen_name': 'whistleblower',},
                     'created_at': datetime.strftime(DT,'%a %b %d %H:%M:%S +0000 %Y'),
                     }
        self.assertEqual(tweet2,expected)



# Test for valid tweets

class TestParsingOfTweets(TestCase):

    def test_tweet1_results(self):

        parse1 = parse_and_store_tweet(tweet1)

        self.assertEqual('',parse1['company_name'])
        self.assertEqual('',parse1['reason'])
        self.assertEqual('',parse1['message'])
        self.assertFalse('',parse1['valid'])

    def test_tweet2_results(self):

        parse2 = parse_and_store_tweet(tweet2)

        self.assertEqual('companyname',parse2['company_name'])
        self.assertEqual('reason',parse2['reason'])
        self.assertEqual('this company is bad',parse2['message'])
        self.assertTrue(parse2['valid'])

# Test saving worked

class TestStoringOfTweets(TestCase):

    def test_storage_basic(self):
        Voice.objects.all().delete()

        parse_and_store_tweet(tweet1)
        parse_and_store_tweet(tweet2)

        storage = Voice.objects.all()
        self.assertEqual(1,len(storage))

        for v in storage:
            self.assertEqual(v.user,'whistleblower')
            self.assertEqual(v.date_added,DT.date())
            self.assertEqual(v.offender,'companyname')
            self.assertEqual(v.reason,'reason')
            self.assertEqual(v.message,'this company is bad')
            self.assertEqual(v.naughty,True)
            self.assertEqual(v.fuzzy,True)
            self.assertEqual(v.verified,False)

    def test_more_than_one_tweet_in_day_by_same_user(self):

        Voice.objects.all().delete()

        parse_and_store_tweet(tweet2)
        parse_and_store_tweet(tweet2)

        storage = Voice.objects.all()
        self.assertEqual(1,len(storage))

        for v in storage:
            self.assertEqual(v.user,'whistleblower')
            self.assertEqual(v.date_added,DT.date())
            self.assertEqual(v.offender,'companyname')
            self.assertEqual(v.reason,'reason')
            self.assertEqual(v.message,'this company is bad')
            self.assertEqual(v.naughty,True)
            self.assertEqual(v.fuzzy,True)
            self.assertEqual(v.verified,False)


    def test_more_than_one_tweet_in_day_by_different_users(self):

        Voice.objects.all().delete()

        parse_and_store_tweet(tweet2)
        parse_and_store_tweet(tweet3)

        storage = Voice.objects.all()
        self.assertEqual(2,len(storage))

        v = storage[0]
        self.assertEqual(v.user,'whistleblower')
        self.assertEqual(v.date_added,DT.date())
        self.assertEqual(v.offender,'companyname')
        self.assertEqual(v.reason,'reason')
        self.assertEqual(v.message,'this company is bad')
        self.assertEqual(v.naughty,True)
        self.assertEqual(v.fuzzy,True)
        self.assertEqual(v.verified,False)

        v = storage[1]
        self.assertEqual(v.user,'goodguy')
        self.assertEqual(v.date_added,DT.date())
        self.assertEqual(v.offender,'companyname')
        self.assertEqual(v.reason,'reason')
        self.assertEqual(v.message,'this company is bad')
        self.assertEqual(v.naughty,True)
        self.assertEqual(v.fuzzy,True)
        self.assertEqual(v.verified,False)