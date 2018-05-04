from django.http import HttpResponse
from scores.models import Scores
from django.shortcuts import render


def index(request):
    score_list = Scores.objects.order_by("composer")[:]
    context = {'score_list': score_list}
    return render(request, 'index.html', context)


def score_viewer(request, composer):
    score_object = Scores.objects.filter(composer=composer)
    context = {'score_object': score_object[0]}
    #print(score_object[0].composer)
    return render(request, 'score_viewer.html', context)
