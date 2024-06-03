from django.db import models

# Create your models here.
class Things_to_do(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    task_image = models.ImageField(upload_to="task")
    
    def __str__(self):
        return self.task_name