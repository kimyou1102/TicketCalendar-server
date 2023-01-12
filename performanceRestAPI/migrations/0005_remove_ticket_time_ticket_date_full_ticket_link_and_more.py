# Generated by Django 4.1.4 on 2023-01-12 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performanceRestAPI', '0004_alter_ticket_performance_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='time',
        ),
        migrations.AddField(
            model_name='ticket',
            name='date_full',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='link',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='performance_info',
            field=models.CharField(max_length=300, null=True, unique=True),
        ),
    ]
