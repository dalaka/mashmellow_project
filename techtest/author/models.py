from django.db import models

# Create your models here.
class Author(models.Model):
    """Author Entity"""
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.first_name