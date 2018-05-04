from django.db import models


class Scores(models.Model):
    composer = models.CharField(max_length=200)
    scorePDF = models.FileField()
    scoreMEI = models.FileField()
