from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    category = models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    Post_id = models.ForeignKey('Post', on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content[:50]