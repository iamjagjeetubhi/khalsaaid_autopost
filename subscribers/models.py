from django.db import models

# Create your models here.

class Subscribers(models.Model):
    username = models.CharField(max_length=200, blank=True)
    dpUrl = models.CharField(max_length=1000, blank=True)
    photoUrl = models.CharField(max_length=1000, blank=True)

    def __str__(self):            
        return self.username

    
class Posts(models.Model):
    post_id = models.CharField(max_length=200, blank=True)
    created_date = models.CharField(max_length=200, blank=True)
    created_time = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=10000, blank=True)

class EmailSent(models.Model):
	post_id = models.CharField(max_length=200, blank=True)
