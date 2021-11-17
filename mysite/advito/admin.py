from django.contrib import admin
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.db.models import fields
from .models import Profile, Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fields = ['author', 'title', 'description', 'image', 'date_pub', 'date_edit','price', 'category']
    fieldsets = [
        ["Основная информация", {'fields': ['author', 'title', 'date_edit', 'date_pub']}],
        ["Детальная информация", {'fields': ['description', 'category', 'price', 'image']}]
    ]
    readonly_fields = ['date_edit', 'date_pub']
    list_display = ['id', 'title', 'author', 'date_pub', 'price', 'category']
    list_display_links = ['id']
    list_filter = ['author', 'category']
    search_fields = ['title']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # fields = ['user', 'id', 'about', 'avatar', 'birth_date', 'created', 'post']
    fieldsets = [
        ["Основная информация", {'fields': [('user', 'birth_date', 'created')]}],
        ["Детальная информация", {'fields': ['about', 'avatar', 'post']}]
    ]
    #  Сделать проперти чтобы при выборе поста был только  те посты которые связаны с профилем
    readonly_fields = ['created']
    list_display = ['id', 'user', 'birth_date', 'created']
    list_display_links = ['id']
    search_fields = ['user', 'birth_date']
    list_filter = ['created', 'birth_date']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id']
    search_fields = ['title']
    list_filter = ['title']

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     fieldsets = [
#         ["Основная информация", {'fields': [('user', 'birth_date', 'created')]}],
#         ["Детальная информация", {'fields': ['about', 'avatar', 'post']}]
#     ]
#     #  Сделать проперти чтобы при выборе поста был только  те посты которые связаны с профилем
#     readonly_fields = ['created']
#     list_display = ['id', 'user', 'birth_date', 'created']
#     list_display_links = ['id']
#     search_fields = ['user', 'birth_date']
#     list_filter = ['created', 'birth_date']
#     form = ProfileInlineForm

# @admin.register(User)
# class MyUserAdmin(UserAdmin):
#     inlines = [ProfileInline]

# class ProfileInlineForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#
#         widgets = {
#             'about': forms.Textarea(attrs={'rows': 4, 'cols': 10})
#         }
#         fields = '__all__'