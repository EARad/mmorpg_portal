from django.contrib import admin

from .models import Category, Ad, News, Reply


# Register your models here.

admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Reply)
admin.site.register(News)
