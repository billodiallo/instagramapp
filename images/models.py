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

    def __str__(cls):
        images = Image.objects.all()
        return images

class Comment(models.Model):
        poster = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
        image = models.ForeignKey(Image,on_delete=models.CASCADE,
        related_name='comments' ,null=True)
        Comment = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment 

class Follow(models.Model):
    users=models.ManyToManyField(User,related_name='follow')
    current_user=models.ForeignKey(User,related_name='c_user',null=True)

@classmethod
    def follow(cls,current_user,new):
        friends,created=cls.objects.get_or_create(current_user=current_user)
        friends.users.add(new)

@classmethod
    def unfollow(cls,current_user,new):
        friends,created=cls.objects.get_or_create(current_user=current_user)
        friends.users.remove(new)
