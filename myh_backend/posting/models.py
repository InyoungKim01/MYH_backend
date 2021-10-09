from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.

class Posting(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    post_title = models.TextField(blank=True)
    post_text = models.TextField(blank=True)
    post_created = models.DateTimeField(auto_now_add=True)
    #updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "text : "+self.post_title

    class Meta:
        ordering = ['-post_created']


    def get_absolute_url(self):
        return reverse('posting:detail', args=[self.id])

