# Generated by Django 4.2.6 on 2024-09-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jointogroup',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
