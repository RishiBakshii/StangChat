from itertools import chain
import random
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .models import Profile,Post,Stang,Followers,Likepost,Likestang
from .helpers import send_forget_password_mail
import uuid

# Create your views here.
@login_required(login_url='/login')
def homepage(r):
    user_obj=User.objects.get(username=f'{r.user}')
    profile_obj=Profile.objects.get(username=f"{user_obj.username}")


    following_list=[]
    feed_list=[]
    result_list=Followers.objects.filter(username=f'{r.user.username}')
    for i in result_list:
        following_list.append(i.user_being_followed)
    
    following_list.append(f'{r.user.username}')
    for i in following_list:
        names=Post.objects.filter(username=i)
        feed_list.append(names)
    
    feed_list=list(chain(*feed_list))

    stang_feed_list=[]
    for i in following_list:
        tt=Stang.objects.filter(username=i)
        stang_feed_list.append(tt)
    stang_feed_list=list(chain(*stang_feed_list))

    user_following=Followers.objects.filter(username=f'{r.user.username}')
    user_following_list=[]

    for i in user_following:
        user_following_list.append(i.user_being_followed)
    
    all_users=Profile.objects.all()
    all_users_list=[]

    for i in all_users:
        all_users_list.append(i.username)

    final_names_to_suggest=[i for i in all_users_list if i not in user_following_list]
    final_names_to_suggest.remove(f'{r.user.username}')

    recommendation_list=[]
    for i in final_names_to_suggest:
        result=Profile.objects.filter(username=i)
        recommendation_list.append(result)

    recommendation_list=list(chain(*recommendation_list))
    random.shuffle(recommendation_list)
    random.shuffle(feed_list)



    return render(r,'homepage.html',{'profile':profile_obj,'post':feed_list,'stang':stang_feed_list,'suggestion':recommendation_list[:30]})

def signuppage(r):
    if r.method=='POST':
        username=r.POST['username']
        password=r.POST['password']
        confirmpassword=r.POST['confirmpassword']
        email=r.POST['email']

        if username=='' or password=='' or confirmpassword==''or email=='':
            messages.info(r,'all input fields are required')
        else:
            
            if password!=confirmpassword:
                messages.info(r,'Passwords do not match')
            
            elif User.objects.filter(username=username).exists():
                messages.info(r,'Username already taken')
            
            elif User.objects.filter(email=email).exists():
                messages.info(r,'Email already taken')
            
            else:
                new_user=User.objects.create_user(username=username,email=email,password=password)
                new_user.save()
                new_profile=Profile.objects.create(username=username)
                new_profile.save()
                login(r,new_user)
                return redirect('/settings')
    
    return render(r,'signup.html')

def loginpage(r):
    if r.method=='POST':
        username=r.POST['username']
        password=r.POST['password']
        user=authenticate(r,username=username,password=password)
        if user is not None:
            login(r,user)
            return redirect('/')
        else:
            messages.info(r,'Invalid Credentials')
            return redirect('/login')
    return render(r,'login.html')

@login_required(login_url='/login')
def logoutpage(r):
    logout(r)
    return redirect('/login')

@login_required(login_url='/login')
def settings(r):
    if r.method=='POST':
        if r.FILES.get('profile-img')==None:
            bio=r.POST['bio']
            location=r.POST['location']
            profile_obj=Profile.objects.get(username=f'{r.user}')
            profile_obj.bio=bio
            profile_obj.location=location
            profile_obj.save()
            return redirect('/settings')
        else:
            profileimg=r.FILES['profile-img']
            bio=r.POST['bio']
            location=r.POST['location']
            profile_obj=Profile.objects.get(username=f'{r.user}')
            profile_obj.profile_pic=profileimg
            profile_obj.bio=bio
            profile_obj.location=location
            profile_obj.save()
            return redirect('/settings')
    profile_obj=Profile.objects.get(username=f'{r.user}')
    return render(r,'settings.html',{'profile':profile_obj})

@login_required(login_url='/login')
def upload(r):
    if r.method=='POST':
        if r.FILES.get('postimage') == None:
            return redirect('/')
        else:
            image=r.FILES['postimage']
            caption=r.POST['caption']
            profile_img=Profile.objects.get(username=f'{r.user}')
            profile_img=profile_img.profile_pic
            
            new_post=Post.objects.create(username=f'{r.user}',post_image=image,caption=caption,profile_image=profile_img)
            new_post.save()
            profile_obj=Profile.objects.get(username=f'{r.user}')
            profile_obj.number_of_posts+=1
            profile_obj.save()

            return redirect('/')

@login_required(login_url='/login')
def uploadstang(r):
    if r.method=='POST':
        if r.POST.get('stangcontent')=='':
            return redirect('/')
        else:
            username=f'{r.user}'
            stangcontent=r.POST['stangcontent']
            new_stang=Stang.objects.create(username=username,stangmessage=stangcontent)
            new_stang.save()
            return redirect('/')

@login_required(login_url='/login')
def viewprofile(r,user):
    all_post=Post.objects.filter(username=user)
    if Followers.objects.filter(username=f'{r.user.username}',user_being_followed=user).exists():
        buttontxt='Unfollow'
    else:
        buttontxt='Follow'
    number_of_followers=len(Followers.objects.filter(user_being_followed=user))
    number_of_following=len(Followers.objects.filter(username=user))
    if Profile.objects.filter(username=user).exists():
        profile_obj=Profile.objects.get(username=user)

        #for following
        user_following=Followers.objects.filter(username=user)
        user_following_names=[]
        user_following_profile_objs=[]
        for i in user_following:
            user_following_names.append(i.user_being_followed)
        for i in user_following_names:
            following_profiles=Profile.objects.filter(username=i)
            user_following_profile_objs.append(following_profiles)
        user_following_profile_objs=list(chain(*user_following_profile_objs))



        followers=Followers.objects.filter(user_being_followed=user)
        followers_names=[]

        for i in followers:
            followers_names.append(i.username)
    
        followers_names_obj=[]

        for i in followers_names:
            hh=Profile.objects.filter(username=i)
            followers_names_obj.append(hh)
        followers_names_obj=list(chain(*followers_names_obj))
        return render(r,'profile.html',{'profile':profile_obj,'buttontxt':buttontxt,'number_of_followers':number_of_followers,'number_of_following':number_of_following,'post':all_post,'followingprofiles':user_following_profile_objs,'user':user,'followersprofiles':followers_names_obj})
    else:
        return HttpResponse('error! @user not found')

@login_required(login_url='/login')
def followupdate(r):
    if r.method=='POST':
        username=r.POST['username']
        user_being_followed=r.POST['user_being_followed']
        update=Profile.objects.get(username=f'{user_being_followed}')
        if Followers.objects.filter(username=username,user_being_followed=user_being_followed).exists():
            delete=Followers.objects.get(username=username,user_being_followed=user_being_followed)
            delete.delete()

            update.followers=update.followers-1
            update.save()

            return redirect(f'/profile/{user_being_followed}')
        else:
            new_follower=Followers.objects.create(username=username,user_being_followed=user_being_followed)
            new_follower.save()
            update.followers+=1
            update.save()
            return redirect(f'/profile/{user_being_followed}')

@login_required(login_url='/login')
def likepost(r):
    username=r.GET['username']
    post_id=r.GET['postid']
    post_obj=Post.objects.get(id=post_id)
    print(post_id,username)

    if Likepost.objects.filter(username=username,post_id=post_id).first():
        hh=Likepost.objects.get(username=username,post_id=post_id)
        hh.delete()
        post_obj.no_of_likes=post_obj.no_of_likes-1
        post_obj.save()
        return redirect('/')
    else:
        new_like=Likepost.objects.create(username=username,post_id=post_id)
        new_like.save()
        post_obj.no_of_likes+=1
        post_obj.save()
        return redirect('/')

@login_required(login_url='/login')
def deletepost(r):
    if r.method=='POST':
        username=r.POST['username']
        postid=r.POST['postid']

        post_obj=Post.objects.get(username=username,id=postid)
        post_obj.delete()

        profile_obj=Profile.objects.get(username=username)
        profile_obj.number_of_posts=profile_obj.number_of_posts-1
        profile_obj.save()
        if Likepost.objects.filter(post_id=postid,username=username).exists():
            like_obj=Likepost.objects.get(post_id=postid,username=username)
            like_obj.delete()
        return redirect('/')

@login_required(login_url='/login')
def deletestang(r):
    username=r.GET['username']
    stangid=r.GET['stangid']

    if Likestang.objects.filter(stang_id=stangid).exists():
        ww=Likestang.objects.get(stang_id=stangid)
        ww.delete()   

    stang_obj=Stang.objects.get(username=username,id=stangid)
    stang_obj.delete()

    return redirect('/')

@login_required(login_url='/login')
def likestang(r):
    username=r.GET['username']
    stangid=r.GET['stangid']
    Stang_obj=Stang.objects.get(id=stangid)


    if Likestang.objects.filter(username=username,stang_id=stangid).exists():
        ee=Likestang.objects.get(username=username,stang_id=stangid)
        ee.delete()
        Stang_obj.number_of_likes=Stang_obj.number_of_likes-1
        Stang_obj.save()
        return redirect('/')
    else:
        new_stang_like=Likestang.objects.create(username=username,stang_id=stangid)
        new_stang_like.save()
        Stang_obj.number_of_likes+=1
        Stang_obj.save()
        return redirect('/')

@login_required(login_url='/login')
def search(r):
    if r.method=='POST':
        username=r.POST['username']
        profile_obj=Profile.objects.get(username=f"{r.user.username}")
        profile_objs=Profile.objects.filter(username__icontains=username)


        user_list=[]
        final_search_results=[]

        for usernames in profile_objs:
            user_list.append(usernames.username)
        
        for i in user_list:
            hh=Profile.objects.filter(username=i)
            final_search_results.append(hh)
        
        final_search_results=list(chain(*final_search_results))

    return render(r,'search.html',{'search':final_search_results,'profile':profile_obj})

@login_required(login_url='/login')
def uploadvideo(r):
    if r.method=='POST':
        if r.FILES.get('postvideo')==None:
            return redirect('/')
        
        else:
            video=r.FILES['postvideo']
            caption=r.POST['videocaption']
            profileimg=Profile.objects.get(username=f'{r.user.username}')
            profileimg=profileimg.profile_pic

            new_video_post=Post.objects.create(username=f'{r.user.username}',post_video=video,caption=caption,profile_image=profileimg)
            new_video_post.save()

            user_profile=Profile.objects.get(username=f'{r.user.username}')
            user_profile.number_of_posts+=1
            user_profile.save()

            return redirect('/') 

@login_required(login_url='/login')       
def deleterequest(r):
    if r.method=='POST':
        userreponse=r.POST['userresponse']
        userreponse=userreponse.replace(' ','')

        if userreponse==f'{r.user.username}/delete':

            profile_obj=Profile.objects.filter(username=f'{r.user.username}')
            profile_obj.delete()

            user_obj=User.objects.filter(username=f'{r.user.username}')
            user_obj.delete()

            if Post.objects.filter(username=f'{r.user.username}').exists():
                post_obj=Post.objects.filter(username=f'{r.user.username}')
                post_obj.delete()
            
            if Stang.objects.filter(username=f'{r.user.username}').exists():
                stang_obj=Stang.objects.filter(username=f'{r.user.username}')
                stang_obj.delete()
            
            if Followers.objects.filter(username=f'{r.user.username}').exists():
                followers_obj=Followers.objects.filter(username=f'{r.user.username}')
                followers_obj.delete()

            if Followers.objects.filter(user_being_followed=f'{r.user.username}').exists():
                followers_objj=Followers.objects.filter(user_being_followed=f'{r.user.username}')
                followers_objj.delete()
            
            if Likepost.objects.filter(username=f'{r.user.username}').exists():
                likepost_obj=Likepost.objects.filter(username=f'{r.user.username}')
                likepost_obj.delete()
            
            if Likestang.objects.filter(username=f'{r.user.username}').exists():
                likestang_obj=Likestang.objects.filter(username=f'{r.user.username}')
                likestang_obj.delete()
            
            logout(r)
            return redirect('/login')
        
        else:
            messages.info(r,'Invalid Input!')
            return redirect('/settings')


    

    




    






