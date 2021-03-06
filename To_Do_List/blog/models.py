# python manage.py sqlmigrate blog 0001
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now_add= True)
    date_posted = models.DateTimeField(default=timezone.now)
    


    def __str__(self):
        return self.title
  
    def save(self):
        super().save()


    

    def get_absolute_url(self):
        return reverse("blog-home")
    