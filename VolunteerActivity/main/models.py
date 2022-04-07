from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='ФИО')
    quest = models.TextField(blank=False, verbose_name='Вопрос')
    answer = models.TextField(blank=True, verbose_name='Ответ')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    class Meta:
        verbose_name = 'Вопросы ответы'
        verbose_name_plural = 'Вопросы ответы'
        ordering = ['time_create', 'time_update']

class Team(models.Model):
    fullName = models.CharField(max_length=255, blank=False, verbose_name='ФИО')
    profession = models.TextField(blank=True, verbose_name='Профессия')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команда'
        ordering = ['time_create', 'time_update']


class Vacancy(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Вакансия')
    text = models.TextField(blank=False, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'
        ordering = ['time_create', 'time_update']
