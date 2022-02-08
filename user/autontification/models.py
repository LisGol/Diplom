import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# def get_file_path(instance, image_name):
#     ext = image_name.split('.')[-1]
#     new_name = f'{uuid.uuid4()}.{ext}'
#     return os.path.join('uploads', 'avatars', new_name)


# class User(AbstractUser):
#     avatar = models.ImageField(
#         verbose_name="Аватар",
#         # upload_to=get_file_path,
#         blank=True,
#         null=True)
#     email = models.EmailField(verbose_name="email", unique=True)

class User(AbstractUser):
    avatar = models.ImageField(verbose_name="Аватарка", blank=True, null=True)
    email = models.EmailField(verbose_name="email", unique=True)

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     bio = models.TextField(null=True, blank=True)
#     profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
#     facebook = models.CharField(max_length=50, null=True, blank=True)
#     twitter = models.CharField(max_length=50, null=True, blank=True)
#     instagram = models.CharField(max_length=50, null=True, blank=True)
#
#
# def __str__(self):
#     return str(self.user)