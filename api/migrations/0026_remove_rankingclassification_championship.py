# Generated by Django 4.1.1 on 2022-12-11 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_team_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rankingclassification',
            name='championship',
        ),
    ]
