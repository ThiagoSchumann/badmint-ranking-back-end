# Generated by Django 4.1.1 on 2022-12-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_rankingclassification_category_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='championship_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='rankingclassification',
            name='period_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]