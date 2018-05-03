from django.http import HttpResponse
from scores.models import Scores
from django.shortcuts import render


def index(request):
    score_list = Scores.objects.order_by("composer")[:]
    context = {'score_list': score_list}
    return render(request, 'scores.html', context)
