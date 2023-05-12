from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
