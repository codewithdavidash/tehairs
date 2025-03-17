from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    image = models.ImageField(upload_to="static/images/blogs")
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ('-created_at',)


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment')

    def __str__(self):
        return self.comment

