from django.db import models
from django.conf import settings
import itertools
from collections import Counter
from datetime import datetime, date

class NaughtyListManager(models.Manager):
    def all(self, size=settings.NAUGHTY_LIST_SIZE, start_date=date(1, 1, 1), end_date=datetime.today()):
        # get a list of key/value pairs, e.g. [{"offender": "badcompany"}, {"offender": "badcompany2"}]
        voices = super(NaughtyListManager, self).get_queryset().filter(naughty=True).distinct().values("offender")
        voices = voices.filter(date_added__range=(start_date, end_date))
        # then turn this into a list of lists, e.g. [["badcompany"], ["badcompany2"]]
        voices = [x.values() for x in voices]
        # flatten the list
        badcompanies = list(itertools.chain(*voices))
        # give a sorted list of pairs of company / number of occurences
        sortedlist = Counter(badcompanies).most_common(size)
        # return just a list of companies
        return [x[0] for x in sortedlist]

class Voice(models.Model):

    user = models.TextField()
    datetime_added = models.DateTimeField(auto_now_add=True)
    date_added = models.DateField(auto_now_add=True)
    offender = models.TextField()
    reason = models.TextField()
    message = models.TextField()
    naughty = models.BooleanField()
    fuzzy = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    objects = models.Manager()
    naughty_list = NaughtyListManager()

class CompanyMapping(models.Model):

    current_name = models.TextField()
    correct_name = models.TextField()