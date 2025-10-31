from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.CharField(max_length=100)
    image=models.ImageField(upload_to="post_images/", blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class TermsOfUse(models.Model):
    title=models.CharField(max_length=200)
    content = models.TextField()
    date_updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_updated = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
