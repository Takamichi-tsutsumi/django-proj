from django.db import models

class Subject(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    point = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

