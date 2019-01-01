from django.db import models
 
class Hit(models.Model):
    hit_count = models.IntegerField()