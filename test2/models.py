from django.db import models
from djrichtextfield.models import RichTextField

class Post(models.Model):
    content = RichTextField()

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateField()
    content = RichTextField()

    def __str__(self):
        return self.title


