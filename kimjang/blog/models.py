from django.db import models
from django.utils import timezone

# Create your models here.
class Hashtag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hashtag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:30]

class Comment(models.Model):
    post=models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author_name=models.CharField(max_length=200)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text