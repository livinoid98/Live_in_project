from django.db import models

# Create your models here.
class Diary(models.Model):
    # User_id = models.ForeignKey('User')
    date = models.DateField()
    title = models.CharField(max_length=20)
    content = models.TextField()
    emotion = models.IntegerField()
    WBC = models.IntegerField()
    RBC = models.IntegerField()
    PT = models.IntegerField()
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Calendar(models.Model):
    # User_id = models.ForeignKey('User')
    datetime = models.DateTimeField()
    hospital = models.CharField(max_length=20)
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content[:10]