from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    prepopulated_fields = {"Slug" : ("Title",)}
    list_filter = ("Title","Author")
    list_display = ("Title", "Date","Author")
    
admin.site.register(Post,BookAdmin)
admin.site.register(Author,)
admin.site.register(Tag,)
