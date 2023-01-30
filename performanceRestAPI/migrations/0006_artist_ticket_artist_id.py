# Generated by Django 4.1.4 on 2023-01-29 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performanceRestAPI', '0005_remove_ticket_time_ticket_date_full_ticket_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='artist_id',
            field=models.ForeignKey(db_column='artist_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='performanceRestAPI.artist'),
        ),
    ]
