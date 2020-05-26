from django.shortcuts import render

from cwPoll.models import Poll
from django.utils import timezone
from django.db.models import Max
import random
from .models import Link, Motd, Member
# Create your views here.

def index(request):
    recentPolls = Poll.objects.filter(
        pollDate__lte = timezone.now()
    ).order_by('-pollDate')[:2]
    allLinks = Link.objects.all()
    allMembers = Member.objects.all()
    thisMotd = fetchRandomMotd()
    context = {
        'recentPolls': recentPolls,
        'allLinks': allLinks,
        'allMembers': allMembers,
        'thisMotd': thisMotd,
    }
    return render(request, 'home/index.html', context)

def fetchRandomMotd():
    maxId = Motd.objects.all().aggregate(maxId = Max('id'))['maxId']
    if not maxId:
        return None
    while True:
        chosenId = random.randint(1,maxId)
        thisMotd = Motd.objects.filter(pk = chosenId).first()
        if thisMotd:
            return thisMotd
