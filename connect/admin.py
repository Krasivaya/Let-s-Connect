from django.contrib import admin
from .models import Author, Post

# Registering Models to Admin.
admin.site.register(Author)
admin.site.register(Post)
