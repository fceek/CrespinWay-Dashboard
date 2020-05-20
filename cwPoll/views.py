from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F, Max
from django.utils import timezone

from .models import Poll, Choice

def index(request):
    recentPolls = Poll.objects.filter(
        pollDate__lte = timezone.now()
    ).order_by('-pollDate')[:10]
    context = {
        'recentPolls': recentPolls,
    } 
    return render(request, 'cwPoll/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk = poll_id)
    return render(request, 'cwPoll/detail.html', {
        'poll': poll
    })

def result(request, poll_id):
    poll = get_object_or_404(Poll, pk = poll_id)
    highestVote = poll.choice_set.all().aggregate(Max('votes'))
    return render(request, 'cwPoll/result.html', {
        'poll': poll,
        'highestVote': highestVote['votes__max'],
    })

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk = poll_id)
    try:
        selectedChoice = poll.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'cwPoll/detail.html', {
            'poll': poll,
            'error_message': "Please choose one of them",
        })
    else:
        selectedChoice.votes = F('votes') + 1
        selectedChoice.save()
        return HttpResponseRedirect(reverse('cwPoll:result', args=(poll.id,)))