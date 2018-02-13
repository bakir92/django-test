from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length = 100)
#     last_name = models.CharField(max_length = 100)
#     email = models.EmailField(max_length = 264,unique = True)
#
#     def __str__(self):
#         return self.email

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    #Additional information
    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = "profile_pics",blank = True)

    def __str__(self):
        return self.user.username
