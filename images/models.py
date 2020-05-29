from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_photo=models.ImageField(upload_to='profiles/',null=True)
    bio= models.CharField(max_length=240,null=True)

    def save_profile(self):
        self.save()
    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile 

    @classmethod
    def find_profile(cls,search_term):
         profile = Profile.objects.filter(user_username__icontains=search_term)
         return profile


class Image(models.Model):
    posted_by = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    inst_image = models.ImageField(upload_to='pitch/' ,null=True)
    caption = models.TextField(null=True)
    likes = models.PositiveIntegerField(default=0)

    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images