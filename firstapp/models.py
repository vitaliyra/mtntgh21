from django.db import models
 
class Hit(models.Model):
    hit_count = models.IntegerField()
	
    def __str__(self):
        return 'Сайт посетили %s раз' % (str(self.hit_count))
