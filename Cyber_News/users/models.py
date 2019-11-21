from django.db import models
from django.contrib.auth.models import (AbstractUser)


# Create your models here.

class User(AbstractUser):
    userImg = models.ImageField(upload_to='user_avas/', default='NULL')

    def __str__(self):
        return self.username


'''class MyUserManager(BaseUserManager):
    def create_user(self, password=None):
        user = self.model()
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password=None):
        user = self.create_user(
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    def __str__(self):
        return self.get_username()'''

'''
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
'''
