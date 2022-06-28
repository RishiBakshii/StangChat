from django.contrib import admin
from .models import Profile,Post,Stang,Followers,Likepost,Likestang

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Stang)
admin.site.register(Followers)
admin.site.register(Likepost)
admin.site.register(Likestang)