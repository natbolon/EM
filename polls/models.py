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
    weight = models.DecimalField(decimal_places=2, max_digits=4, default=None)
    height = models.DecimalField(decimal_places=1, max_digits=4, default=None)
    gender = models.TextField(choices=[(None, 'Select a gender'), ('M', 'Male'), ('F', 'Female')], default=None)
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


class DynamicParams(models.Model):
    front_camber = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    rear_camber = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    front_toe = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    rear_toe = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    front_pressure = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    rear_pressure = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    front_weight = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    rear_weight = models.DecimalField(decimal_places=2, max_digits=4, default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.id


class AerodynamicsParams(models.Model):
    fw_flap1_degrees = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    fw_flap2_degrees = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    rw_flap1_degrees = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    rw_flap2_degrees = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    drs = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.id


class PowertrainParams(models.Model):
    mode = models.DecimalField(decimal_places=0, max_digits=2, default=0)
    cont_current_p = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    peak_current_p = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    kp_current = models.DecimalField(decimal_places=0, max_digits=5, default=0)
    ti_current = models.DecimalField(decimal_places=0, max_digits=5, default=0)
    kp_speed = models.DecimalField(decimal_places=0, max_digits=5, default=0)
    ti_speed = models.DecimalField(decimal_places=0, max_digits=5, default=0)

    class Meta:
        abstract = True

    def __str__(self):
        return self.id


class Testing(DynamicParams, AerodynamicsParams, PowertrainParams):
    when = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200, default="")
    event = models.TextField(choices=[('Acceleration', 'Acceleration'), ('Skid Pad', 'Skid Pad'),
                                      ('Autocross', 'Autocross'), ('Endurance', 'Endurance')],
                             default='Acceleration')
    comments = models.TextField(max_length=2000, default="")

    # driver = models.ForeignKey(Driver.name, related_query_name='driver', on_delete=models.SET('Ghost driver'),
    #                           null=True)

    def __str__(self):
        # return self.time.strftime('%H:%M - %d-%m-%Y')
        return self.id
