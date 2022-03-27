from django.db import models
from django.contrib import auth

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    user_id = models.ForeignKey(auth.get_user_model(),
                                on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE,
                                    verbose_name='Категория')
    header = models.CharField(max_length=255, verbose_name='Заголовок')
    ad = RichTextUploadingField(default='', verbose_name='Объявление')
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header


class Reply(models.Model):
    user_id = models.ForeignKey(auth.get_user_model(),
                                on_delete=models.CASCADE)
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    reply = models.TextField(default='', verbose_name='Отклик')
    creation_time = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.reply


class News(models.Model):
    user_id = models.ForeignKey(auth.get_user_model(),
                                on_delete=models.CASCADE)
    header = models.CharField(max_length=255, verbose_name='Заголовок')
    news = RichTextUploadingField(default='', verbose_name='Новость')
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.header


def return_user_email(user):
    return user.email
