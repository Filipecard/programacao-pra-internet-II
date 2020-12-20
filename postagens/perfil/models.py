from django.db import models
from django.db.models.fields import IntegerField

class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, default='')
    email = models.CharField(max_length=200, blank=True, default='')
    
    class Meta:
        ordering = ('name',)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, default='')
    body = models.TextField(blank=True, null=True)
    userId = models.ForeignKey(Perfil, on_delete=models.CASCADE)

    
    class Meta:
        ordering = ('title',)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, default='')
    email = models.CharField(max_length=200, blank=True, default='')
    body = models.TextField(blank=True, null=True)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)

    
    class Meta:
        ordering = ('name',)
