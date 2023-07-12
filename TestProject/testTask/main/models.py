from django.db import models


class Settings(models.Model):
    title = models.CharField('Текст', max_length=255)
    color_text = models.CharField(max_length=7)
    color_back = models.CharField(max_length=7)
    fps = models.IntegerField()
    time = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
