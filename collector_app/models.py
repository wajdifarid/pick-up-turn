from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Collection(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    collector = models.ForeignKey(User,on_delete=models.PROTECT)
    collected_item = models.TextField()
