from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
 
class UserManager(BaseUserManager):
 
    def _create_user(self, email, password):
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise
 
    def create_user(self, email, password=None):
        return self._create_user(email, password)
 
    def create_superuser(self, email, password):
        return self._create_user(email, password=password)
 
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
 
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
