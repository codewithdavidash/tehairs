# from django.contrib.auth.models import User
from django.db import models


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=11)
#     billing_address = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='static/images/profile_pictures', default='static/images/default.png')
#     created_at = models.DateTimeField(auto_now_add=True)
#     modified_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         ordering = ('-created_at',)
        
#     def __str__(self):
#         # return self.user.username