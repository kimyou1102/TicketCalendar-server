# Generated by Django 4.1.4 on 2023-01-31 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performanceRestAPI', '0007_alter_artist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='link',
            field=models.URLField(max_length=500, null=True),
        ),
    ]