import datetime

from django.db import models


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
    front_height = models.DecimalField(decimal_places=2, max_digits=4, default=0)
    rear_height = models.DecimalField(decimal_places=2, max_digits=4, default=0)

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
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200, default="")
    event = models.TextField(choices=[('Acceleration', 'Acceleration'), ('Skid Pad', 'Skid Pad'),
                                      ('Autocross', 'Autocross'), ('Endurance', 'Endurance')],
                             default='Acceleration')
    comments = models.TextField(max_length=20000, default="", blank=True)

    driver = models.ForeignKey(Driver, related_query_name='driver', on_delete=models.CASCADE)

    def __str__(self):
        # return self.time.strftime('%H:%M - %d-%m-%Y')
        return str(self.date)

    class Meta:
        order_with_respect_to = 'id'


class Results(models.Model):
    temp_inv_ini = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_inv_end = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_bat_ini = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_bat_end = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_pneu_FL_ini = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_pneu_FR_ini = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_pneu_RL_ini = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_pneu_RR_ini = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_pneu_FL_end = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_pneu_FR_end = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_pneu_RL_end = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_pneu_RR_end = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_motor_ini = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    temp_motor_end = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    volt_min_ini = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    volt_min_end = models.DecimalField(decimal_places=0, max_digits=3, default='', blank=True, null=True)
    comments = models.TextField(max_length=20000, default="", blank=True)

    class Meta:
        abstract = True


class Acceleration(Results):
    id = models.AutoField(primary_key=True)
    length = 75
    time = models.CharField(max_length=7, default="")
    date = models.DateTimeField(auto_now=True)
    params = models.ForeignKey(Testing, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Skid_Pad(Results):
    id = models.AutoField(primary_key=True)
    length_lap = 57.33
    total_length = 229.33
    l1_time = models.CharField(max_length=7, default="")
    l2_time = models.CharField(max_length=7, default="")
    r1_time = models.CharField(max_length=7, default="")
    r2_time = models.CharField(max_length=7, default="")
    date = models.DateTimeField(auto_now=True)
    params = models.ForeignKey(Testing, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    def time(self):
        return int(self.l1_time) + int(self.l2_time) + int(self.r1_time) + int(self.r2_time)


class AutoX(Results):
    id = models.AutoField(primary_key=True)
    length_lap = models.DecimalField(decimal_places=2, max_digits=6, default=100)
    time = models.CharField(max_length=7, default="")
    date = models.DateTimeField(auto_now=True)
    params = models.ForeignKey(Testing, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Endurance(Results):
    id = models.AutoField(primary_key=True)
    length_lap = models.DecimalField(decimal_places=2, max_digits=6, default=100)
    total_length = 22000

    # THINK ABOUT HOW TO HANDLE LAPS. INTENTION: CREATE A VARIABLE (LIST) THAT STORES ALL THE LAP TIMES AND
    # ARISES A WARNING WHEN REACHED THE LAST LAP

    def __str__(self):
        return str(self.id)

    def laps(self):
        return int(self.total_length / self.length_lap)
