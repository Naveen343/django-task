from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    quest_text = models.CharField(max_length=200)
    publi_date = models.DateTimeField("date published")
    def __str__(self):
        return self.quest_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publi_date <= now

    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text
