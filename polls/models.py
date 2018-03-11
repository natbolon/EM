import datetime

from django.db import models


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
    birthday = models.DateField()
    creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    @property
    def compute_age(self):
        delta = datetime.date.today() - self.birthday
        return int(delta.days / 365)

    age = compute_age


class Testing(models.Model):
    # driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200, default="")

    def __str__(self):

        return self.time.strftime('%H:%M - %d-%m-%Y')

    # @property
    # def order(self):
    #    return next(self)


class Acceleration(models.Model, models.Testing):
    front_camber = models.DecimalField(decimal_places=2, max_digits=3, default="")
    rear_camber = models.DecimalField(decimal_places=2, max_digits=3, default="")
    front_toe = models.DecimalField(decimal_places=2, max_digits=3, default="")
    rear_toe = models.DecimalField(decimal_places=2, max_digits=3, default="")
    front_pressure = models.DecimalField(decimal_places=2, max_digits=3, default="")
    rear_pressure = models.DecimalField(decimal_places=2, max_digits=3, default="")
    front_weight = models.DecimalField(decimal_places=2, max_digits=4, default="")
    rear_weight = models.DecimalField(decimal_places=2, max_digits=4, default="")

    def __str__(self):
        return self.models.Testing.date.strftime('%H:%M - %d-%m-%Y')
