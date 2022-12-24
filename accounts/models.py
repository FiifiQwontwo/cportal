from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
# User accounts Manager
class MyAccountManager(BaseUserManager):
    def create_user(self, last_name, username, email, phone, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError("User must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            # first_name=first_name,
            last_name=last_name,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, last_name, email, username, phone, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            # first_name=first_name,
            last_name=last_name,
            phone=phone

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=50)
    # required Fields
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    # I set to False to so i can verified the mail of the user ie is_active is always True when am not verifing a user
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name', 'phone']
    #  u will always need to end the class with() or natural key error awaits
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to='user_profile/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.user.last_name
