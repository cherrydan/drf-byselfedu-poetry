from django.contrib.auth.models import User
from django.db import models


# Модель описания кожаной вещи


class LeatherClothes(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')  # краткое название
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    color = models.CharField(max_length=50, verbose_name='Цвет')  # описание цвета
    size = models.CharField(max_length=50,
                            verbose_name='Размер')  # описание размера = либо цифры (42-44) либо буквы (S/M/L) либо вместе
    length = models.IntegerField(verbose_name='Длина')  # длина изделия в см. тут без вариантов Int
    description = models.CharField(blank=True, max_length=255, verbose_name='Описание')  # детальное описание
    # photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')  # фото изделия, папка, куда будут падать загруженные фото
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создан')  # время создания записи
    time_update = models.DateTimeField(auto_now=True, verbose_name='Обновлён')  # время обновления записи
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')  # флаг, опубликована ли статья
    # поле, ссылающееся на другой класс
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Женская кожаная одежда'
        verbose_name_plural = 'Женская кожаная одежда'
        ordering = ['id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
