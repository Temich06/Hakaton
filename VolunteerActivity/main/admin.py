from django.contrib import admin

from .models import *


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'time_create', 'time_update')
    search_fields = ('id', 'time_create', 'time_update')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'time_create', 'time_update')
    search_fields = ('id', 'time_create', 'time_update')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_create', 'time_update', 'is_published')
    list_display_links = ('id', 'time_create', 'time_update')
    search_fields = ('id', 'time_create', 'time_update')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Vacancy, VacancyAdmin)