from django.db import models


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


class CompanyMapping(models.Model):

    current_name = models.TextField()
    correct_name = models.TextField()