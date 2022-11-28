from django.contrib import admin
from django.apps import apps

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import *

models = apps.get_models()


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'birth_date',
                    'athlete_code',
                    'club')


exclude_models = []

for model in models:
    try:
        if model not in exclude_models:
            admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
