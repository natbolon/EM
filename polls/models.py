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

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']

    @property
    def compute_age(self):
        delta = datetime.date.today() - self.birthday
        return int(delta.days / 365)

    age = compute_age


class Testing(models.Model):
    # driver = models.ForeignKey(Driver.name, related_query_name='driver', on_delete=models.SET('Ghost driver'),
    #                           null=True)
    time = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200, default="")
    event = models.TextField(choices=[('Acceleration', 'Acceleration'), ('Skid Pad', 'Skid Pad'),
                                      ('Autocross', 'Autocross'), ('Endurance', 'Endurance')], default='Acceleration')

    def __str__(self):
        # return self.time.strftime('%H:%M - %d-%m-%Y')
        return self.id



class DynamicParams(models.Model):
    front_camber = models.DecimalField(decimal_places=2, max_digits=3, default="")
    rear_camber = models.DecimalField(decimal_places=2, max_digits=3, default="")
    front_toe = models.DecimalField(decimal_places=2, max_digits=3, default="")
    rear_toe = models.DecimalField(decimal_places=2, max_digits=3, default="")
    front_pressure = models.DecimalField(decimal_places=2, max_digits=3, default="")
    rear_pressure = models.DecimalField(decimal_places=2, max_digits=3, default="")
    front_weight = models.DecimalField(decimal_places=2, max_digits=4, default="")
    rear_weight = models.DecimalField(decimal_places=2, max_digits=4, default="")
    comments = models.TextField(max_length=2000)

    def __str__(self):
        return self.id


class AerodynamicsParams(models.Model):
    fw_flap1_degrees = models.DecimalField(decimal_places=1, max_digits=3, default="")
    fw_flap2_degrees = models.DecimalField(decimal_places=1, max_digits=3, default="")
    rw_flap1_degrees = models.DecimalField(decimal_places=1, max_digits=3, default="")
    rw_flap2_degrees = models.DecimalField(decimal_places=1, max_digits=3, default="")
    drs = models.BooleanField(default=True)
    comments = models.TextField(max_length=2000)

    def __str__(self):
        return self.id


class PowertrainParams(models.Model):
    mode = models.DecimalField(decimal_places=0, max_digits=2, default="")
    cont_current_p = models.DecimalField(decimal_places=1, max_digits=3, default="")
    peak_current_p = models.DecimalField(decimal_places=1, max_digits=3, default="")
    kp_current = models.DecimalField(decimal_places=0, max_digits=5, default="")
    ti_current = models.DecimalField(decimal_places=0, max_digits=5, default="")
    kp_speed = models.DecimalField(decimal_places=0, max_digits=5, default="")
    ti_speed = models.DecimalField(decimal_places=0, max_digits=5, default="")
    comments = models.TextField(max_length=2000)

    def __str__(self):
        return self.id
