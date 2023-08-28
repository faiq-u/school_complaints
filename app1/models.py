from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class complaints(models.Model):
    actual = models.TextField()
    complainer = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    acceptable = models.BooleanField(null=True,blank=True)
    anonyomous = models.BooleanField(default=False,null=True)
    fixed = models.BooleanField(default=False)
    rejected1 = models.BooleanField(null=True,blank=True)
    rejected2 = models.BooleanField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    about = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.actual[0:10]