from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'author', 'text', 'published_date']
	list_display = ('title', 'author', 'published_date')

admin.site.register(Post, PostAdmin)
