from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    author = models.ForeignKey('author.Author', related_name="author", on_delete=models.SET_NULL,null=True, blank=True, default=None)
    regions = models.ManyToManyField(
        'regions.Region', related_name='articles', blank=True
    )
