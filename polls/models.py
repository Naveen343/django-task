from django.db import models
from django.db.models import indexes
import datetime
from django.utils import timezone
import uuid
# Create your models here.
class Question(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4 , editable=False)
    quest_text = models.CharField(max_length=200, db_index=True)
    publi_date = models.DateTimeField("date published", db_index=True)
    def __str__(self):
        return self.quest_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publi_date <= now
    class Meta:
        indexes = [models.Index(fields=[ '-quest_text'])]
  

    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text
