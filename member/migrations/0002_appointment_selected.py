# Generated by Django 3.1.6 on 2021-03-17 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='selected',
            field=models.CharField(choices=[('appointed', 'appointed'), ('not_appointed', 'not_appointed'), ('not_verified', 'not_verified')], default='not_verified', max_length=120),
        ),
    ]