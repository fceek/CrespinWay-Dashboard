from django.db import models
import datetime

# Create your models here.
class Link(models.Model):
    linkTitle = models.CharField(max_length = 100)
    linkUrl = models.URLField()

    def __str__(self):
        return self.linkTitle

class Member(models.Model):
    memberName = models.CharField(max_length = 100)
    memberPhone = models.CharField(max_length = 20)
    memberMail = models.EmailField()
    memberDescription = models.CharField(max_length = 200)
    memberBirth = models.DateField('Birthday', default = datetime.date.today())

    def __str__(self):
        return self.memberName

class Motd(models.Model):
    motdText = models.CharField(max_length = 1000)
    motdSource = models.CharField(max_length = 100)

    def __str__(self):
        return self.motdSource