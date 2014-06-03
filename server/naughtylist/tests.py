from django.conf import settings
from django.test import TestCase
from naughtylist.models import Voice
from datetime import datetime, timedelta

# Create your tests here.

class ListMethodTests(TestCase):
    def setUp(self):
        Voice.objects.create(user="1", offender="badcompany", reason="", message="", naughty=True)
        Voice.objects.create(user="2", offender="badcompany", reason="", message="", naughty=True)
        Voice.objects.create(user="3", offender="baddy", reason="", message="", naughty=True)
        Voice.objects.create(user="4", offender="anotherbadco", reason="", message="", naughty=True)
        Voice.objects.create(user="5", offender="goodcompany", reason="", message="", naughty=False)

    def test_positive_global_list_size_variable_exists(self):
        """
        there should exist a list of X (stored in a global
        settings variable NAUGHTY_LIST_SIZE) companies who
        have the most complaints. X should be > 0
        """
        self.assertGreater(settings.NAUGHTY_LIST_SIZE, 0)
        
    def test_global_list_size_is_integer(self):
        """
        NAUGHTY_LIST_SIZE should be an integer (or long)
        """
        self.assertTrue(isinstance(settings.NAUGHTY_LIST_SIZE, (int, long)))

    def test_only_naughty_complaints_in_list(self):
        """
        only naughty complaints are heard i.e. add naughty=False to some test data
        """
        self.assertIn("badcompany", Voice.naughty_list.all())
        self.assertNotIn("goodcompany", Voice.naughty_list.all())

    def test_list_size_can_be_overwritten(self):
        """
        the ability to override the default NAUGHTY_LIST_SIZE by passing in an argument to the naughty_list method
        """
        self.assertLessEqual(len(Voice.naughty_list.all()), settings.NAUGHTY_LIST_SIZE)
        self.assertEquals(len(Voice.naughty_list.all(size=2)), 2)
        self.assertEquals(len(Voice.naughty_list.all(size=3)), 3)

    def test_date_range_can_be_passed(self):
        """
        the ability to pass in date range (from, to) arguments to the method
        """
        one_day_from_now = datetime.today() + timedelta(days=1)
        two_days_from_now = datetime.today() + timedelta(days=2)
        self.assertEquals(Voice.naughty_list.all(start_date=one_day_from_now, end_date=two_days_from_now), [])
        self.assertGreater(len(Voice.naughty_list.all()), 0)