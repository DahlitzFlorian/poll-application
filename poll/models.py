from django.db import models


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
