from django.db import models
from django.utils import timezone
import random
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    lottos = models.CharField(max_length=255,
                              default='[1,2,3,4,5,6]')
    text = models.CharField(max_length=255)
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()