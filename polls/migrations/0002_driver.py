# Generated by Django 2.0.2 on 2018-03-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('born', models.DateTimeField(verbose_name='born day')),
                ('gender', models.TextField(choices=[('M', 'Male'), ('F', 'Female')])),
                ('registered_data', models.DateTimeField(verbose_name='registered day')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
