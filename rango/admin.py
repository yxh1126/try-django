from django.contrib import admin
from rango.models import Category, Page, UserProfile
# from django.contrib.auth.models import User


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
# admin.site.register(User)
admin.site.register(UserProfile)
