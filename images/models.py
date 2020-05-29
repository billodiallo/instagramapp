#from django.db import models
f#rom django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_photo=models.ImageField(upload_to='profiles/ ,null=True)
    bio= models.CharField(max_length=240,null=True)

    def save_profile():
        self.save()
    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile 

