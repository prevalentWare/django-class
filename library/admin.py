from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, Author, Category

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category',  'published_date')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')

@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)