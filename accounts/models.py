from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Manager(BaseUserManager):
    
    use_in_migrations = True
    
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('No Email!')
        if not username:
            raise ValueError('No Username!')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
    
class User(AbstractBaseUser):
    email = models.EmailField('Email', unique=True, max_length=60)
    username = models.CharField('Username', unique=True, max_length=30)
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)
    last_login = models.DateTimeField('Last Login', auto_now=True)
    is_admin = models.BooleanField('Is Admin', default=False)
    is_active = models.BooleanField('Is Active', default=True)
    is_staff = models.BooleanField('Is Staff', default=False)
    is_superuser = models.BooleanField('Is Superuser', default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]
    
    objects = Manager()
    
    def __str__(self):
        return self.username
    
    # PermissionsMixin
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    