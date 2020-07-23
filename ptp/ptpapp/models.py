from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
 
    def create_user(self, email, password, **extra_fields):
    
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
       
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username=None
    first_name = models.CharField(('first name'), max_length=30, blank=False)
    last_name = models.CharField(('last name'), max_length=150, blank=False)
    email = models.EmailField(('email address'), blank=False,unique=True)
    about=models.TextField(blank=True)
    photo=models.ImageField(blank=True)
    links=models.CharField(max_length=100,blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

class Startups(models.Model):
    startups_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    about=models.TextField()
    user_id =models.ForeignKey(User,on_delete=models.CASCADE)
    links=models.CharField(max_length=100)
    
class Team(models.Model):
    startups_id=models.ForeignKey(Startups,on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    accepted=models.BooleanField()
    
    users=models.ManyToManyField(User)