from django.db import models

from users.models import NULLABLE


class Section(models.Model):
    """Модель Раздела"""
    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.TextField(verbose_name='Description', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ['id']


class Content(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Section')
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(verbose_name='Content')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'
        ordering = ['id']
