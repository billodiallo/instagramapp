from django.test import TestCase
from .models import *

# Create your tests here.

class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='zyzu')
        self.profile = Profile.objects.create(user = self.user,bio = 'blow away')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

    def test_find_profile(self):
        self.profile.save()
        profile = Profile.find_profile('zyzu')
        self.assertTrue(len(profile) > 0)

class ImageTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='zyzu')
        self.profile = Profile.objects.create(user = self.user,bio = 'blow away')

        self.image = Image.objects.create(posted_by = self.user,
                                          profile = self.profile,
                                          caption ='turn up',
                                          likes = 0)

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_get_images(self):
        self.image.save()
        image = Image.get_images()
        self.assertTrue(len(image) == 1)



class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='zyzu')

        self.comment= Comment.objects.create(poster= self.user, comment='new comment' )

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_get_comment(self):
        self.comment.save()
        comment = Comment.get_comment()
        self.assertTrue(len(comment) == 1)