from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (
    BaseUserManager
)
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser
# class User(AbstractUser):
#     empAddress= models.TextField()
class UserManager(BaseUserManager):
    def create_user(self, empEmail, password,empAddress,empName):
        """
        Creates and saves a User with the given email and password.
        """
        if not empEmail:
            raise ValueError('Users must have an email address')

        user = self.model(
            empEmail=self.normalize_email(empEmail),empName=empName,empAddress=empAddress
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class EmpTable(AbstractBaseUser):
    empID=models.AutoField(primary_key=True)
    empName=models.CharField(max_length=150)
    empEmail=models.EmailField()
    password=models.CharField(max_length=100)
    empAddress=models.CharField(max_length=250)
    USERNAME_FIELD = 'empEmail'
    REQUIRED_FIELDS = ['password']
    objects = UserManager()
    class Meta:
        indexes = [
            models.Index(fields=['empID','empEmail', ]),
        ]
