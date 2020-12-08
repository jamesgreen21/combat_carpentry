from django.db import models


class Service(models.Model):
    title = models.CharField(unique=True, max_length=25)
    image = models.ImageField(upload_to='service')
    description = models.CharField(max_length=100)
    post_filter = models.CharField(max_length=10, default='bespoke')

    def __str__(self):
        return self.title


class Post(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=25)
    headline = models.CharField(max_length=50)
    image = models.ImageField(upload_to='post')
    description = models.TextField(null=True)
    customer = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
