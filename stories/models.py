import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Story(models.Model):
  text = models.TextField()
  title = models.CharField(max_length=200)
  approved = models.NullBooleanField(null=True)
  pub_date = models.DateField('date published')
  def __str__(self):
    return self.title
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
