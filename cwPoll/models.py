from django.db import models
from django.utils import timezone

import datetime

# Create your models here.
class Poll(models.Model):
    pollDescription = models.CharField(max_length = 200)
    pollDate = models.DateTimeField('Poll Date')
    pollInDetail = models.CharField(max_length = 500, default = " ")

    def isRecent(self):
        return timezone.now() - datetime.timedelta(days = 1) <= self.pollDate <= timezone.now()

    def __str__(self):
        return self.pollDescription

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete = models.CASCADE)
    choiceDescription = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choiceDescription
    