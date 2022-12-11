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
    list_filter = ('team',
                   'championship',
                   'category',
                   'classification',
                   'score',
                   'expiration_date')


@admin.register(RankingClassification)
class RankingClassificationAdmin(admin.ModelAdmin):
    list_display = ('classification',
                    'scorePoints',
                    'period_date',
                    'category',
                    'category_description',
                    'ranking',
                    'ranking_description',
                    'team',
                    'athlete1MemberID',
                    'athlete1Name',
                    'athlete1Age',
                    'athlete1Club',
                    'athlete2MemberID',
                    'athlete2Name',
                    'athlete2Age',
                    'athlete2Club')
    list_filter = ('classification',
                   'scorePoints',
                   'period_date',
                   'category_description',
                   'ranking_description',
                   'team',
                   'team_name')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('athlete_1',
                    'athlete_2',
                    'category',
                    'name')
    list_filter = ('athlete_1',
                   'athlete_2',
                   'category',
                   'name')
