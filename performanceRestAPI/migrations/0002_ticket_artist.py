# Generated by Django 4.1.4 on 2022-12-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performanceRestAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='artist',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
