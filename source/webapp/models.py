from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=500, verbose_name="Под Заголовок")
    description = models.CharField(max_length=3000, verbose_name="Описание")
    price = models.IntegerField(verbose_name="цена")
    genre = models.CharField(max_length=255, verbose_name="Жанр")
    author = models.CharField(max_length=255, verbose_name="Автор")
    year = models.CharField(max_length=1000, verbose_name="Год выхода книги")
    creation_date = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Дата создания')
    is_favorites = models.ManyToManyField("self", blank=True, related_name='favorites')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


