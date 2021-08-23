from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=255)
    completed=models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.name