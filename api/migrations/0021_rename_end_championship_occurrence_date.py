# Generated by Django 4.1.1 on 2022-12-05 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_classificationscore_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='championship',
            old_name='end',
            new_name='occurrence_date',
        ),
    ]
