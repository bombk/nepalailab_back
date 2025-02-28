from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)

class Carousel(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to='carousel_images/',max_length=100)
    position = models.PositiveIntegerField(default=0)

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,null=True)
    content = HTMLField()
    image = models.FileField(upload_to='post_images/',max_length=100)
    views = models.PositiveIntegerField(default=0)
    auther = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug= models.SlugField(max_length=100, unique=True)
    image = models.FileField(upload_to='project_images/',max_length=100)
    details = HTMLField()
    developer = models.CharField(max_length=100)
    githublink= models.CharField(max_length=500)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=100)
    slug= models.SlugField(max_length=100, unique=True)
    image = models.FileField(upload_to='services_images/',max_length=100)
    details = HTMLField()
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_link = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    name=models.CharField(max_length=500)
    email=models.EmailField(max_length=100)
    number=models.CharField(max_length=10)
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
