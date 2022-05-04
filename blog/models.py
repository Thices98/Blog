from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=255)   #Strings com ate 255 characteres
    slug = models.SlugField(max_length=255, unique=True)    
    # www.site.com/blog/slug
    #cada post possui um slug
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    #Adiciona automaticamente a data e hora do post
    updated = models.DateTimeField(auto_now=True)
    #Atualiza automaticamente a data e hora do post

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail",kwargs={"slug":self.slug})




