from django.db import models
import uuid


# Create your models here.
class Profile(models.Model):
    username=models.CharField(max_length=100)
    following=models.IntegerField(blank=True,default=0)
    followers=models.IntegerField(blank=True,default=0)
    profile_pic=models.ImageField(upload_to='profileImage',default='defaultprofileimg.png',blank=True)
    bio=models.CharField(max_length=100,blank=True)
    location=models.CharField(max_length=100,blank=True)
    number_of_posts=models.IntegerField(blank=True,default=0)


    def __str__(self):
        return self.username

class Post(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True)
    profile_image=models.ImageField(upload_to='postcardimages',default='defaultprofileimg.png')
    username=models.CharField(max_length=100)
    post_image=models.ImageField(upload_to='postImages',blank=True)
    post_video=models.FileField(upload_to='postvideos',blank=True)
    no_of_likes=models.IntegerField(blank=True,default=0)
    caption=models.CharField(max_length=1000000,default='No caption')


    def __str__(self):
        return self.username

class Stang(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    username=models.CharField(max_length=100)
    stangmessage=models.CharField(max_length=1000)
    number_of_likes=models.IntegerField(blank=True,default=0)


    def __str__(self):
        return self.username

class Followers(models.Model):
    username=models.CharField(max_length=100)
    user_being_followed=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Likepost(models.Model):
    username=models.CharField(max_length=100)
    post_id=models.CharField(max_length=1000000)

    def __str__(self):
        return self.username
    
class Likestang(models.Model):
    username=models.CharField(max_length=100)
    stang_id=models.CharField(max_length=1000000)

    def __str__(self):
        return self.username


    
