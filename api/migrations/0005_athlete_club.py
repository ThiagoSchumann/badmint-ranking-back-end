# Generated by Django 4.1.1 on 2022-11-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_file_type_alter_file_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='club',
            field=models.TextField(default=' ', max_length=255, verbose_name='Clube'),
        ),
    ]