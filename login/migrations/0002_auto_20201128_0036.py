# Generated by Django 3.0.3 on 2020-11-28 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lname',
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='default', max_length=100, verbose_name='First name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='default', max_length=100, verbose_name='Last name'),
            preserve_default=False,
        ),
    ]
