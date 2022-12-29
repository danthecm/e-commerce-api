from django.db import models

# Create your models here.


class BaseModel(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Admin(BaseModel):
    is_admin = models.BooleanField(default=True)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Vendor(BaseModel):
    is_vendor = models.BooleanField(default=True)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Customer(BaseModel):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username
