import datetime

from django.db import models
from django.utils import timezone


# Question-Class managing question texts and its publication date
class Question(models.Model):
    # variables beneath represent attributes of the objects
    # as well as columns in the db tables
    question_text = models.CharField(max_length=200)

    # 'date published' as first argument is the human-readable
    # name. If this argument is not given, Django uses the
    # machine-readable name (simply the name of the variable)
    pub_date = models.DateTimeField('date published')


    # objects' representation
    def __str__(self):
        return self.question_text
    

    # defining a simple method
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    # customize was_published_recently() output in admin panel
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# Choice-Class managing to a question the choice text and the
# number of votes
class Choice(models.Model):
    # ForeignKey defines a relationship between each Choice-object
    # and a single question.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # objects' representation
    def __str__(self):
        return self.choice_text
