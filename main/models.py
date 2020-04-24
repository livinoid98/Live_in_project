from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=20)
    zone_category = models.CharField(max_length=20)
    info = models.TextField()
    site_url = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    tel = models.CharField(max_length=15)
    img = models.ImageField()

    def __str__(self):
        return self.name

class Review(models.Model):
    Hospital_id = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    score = models.IntegerField()
    content = models.CharField(max_length=200)
    # User_id = models.ForeignKey('User')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.content[:10]
