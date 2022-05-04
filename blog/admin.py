from django.contrib import admin
from.models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):  #campos para mostrar na tela
    list_display=('title','slug','author','created','updated')
    prepopulated_fields={'slug':("title",)}
