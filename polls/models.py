from django.db import models
from datetime import datetime
from django.utils import timezone


# each class represents a databased field in the model

class Question(models.Model):
    # Field type: CharField or DateTimeField
    # each field name is the one appearing as a column name and the one used for referecing it in the code
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Driver(models.Model):
    name = models.CharField(max_length=200, default="")
    surname = models.CharField(max_length=200, default="")
    email = models.EmailField()
    weight = models.DecimalField(decimal_places=2, max_digits=4, default="")
    height = models.DecimalField(decimal_places=1, max_digits=4, default="")
    gender = models.TextField(choices=[('M', 'Male'), ('F', 'Female')], default='M')
    birthday = models.DateTimeField()
    creation = models.DateTimeField(auto_now=True)
    #updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def age(self):
        return self.creation - self.birthday


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
