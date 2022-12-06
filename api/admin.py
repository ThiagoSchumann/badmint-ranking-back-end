from django.contrib import admin
from django.apps import apps

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'type')


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'birth_date',
                    'athlete_code',
                    'club')


@admin.register(ClassificationScore)
class ClassificationScoreAdmin(admin.ModelAdmin):
    list_display = ('team',
                    'championship',
                    'category',
                    'classification',
                    'score',
                    'expiration_date')


@admin.register(RankingClassification)
class RankingClassificationAdmin(admin.ModelAdmin):
    list_display = ('classification',
                    'scorePoints',
                    'championship',
                    'period_date',
                    'category',
                    'category_description',
                    'ranking',
                    'ranking_description',
                    'athlete1MemberID',
                    'athlete1Name',
                    'athlete1Age',
                    'athlete1Club',
                    'athlete2MemberID',
                    'athlete2Name',
                    'athlete2Age',
                    'athlete2Club')
