# Generated by Django 5.1.3 on 2024-11-17 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_echeance',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
