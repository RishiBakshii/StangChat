from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from pyrsistent import s
from chat.models import Room ,Message
from django.contrib import messages

# Create your views here.
def home(requests):
    return render(requests,'home.html')



def checkview(requests):
    username=requests.POST.get('username')
    roomname=requests.POST.get('roomname')
    if username=='' or roomname=='':
        return redirect('/')

    if Room.objects.filter(name=roomname).exists():
        return redirect(f'{roomname}/?username={username}')
    else:
        new_room=Room.objects.create(name=roomname)
        new_room.save()
        return redirect(f'{roomname}/?username={username}')
        


def roompage(requests,room):
    username=requests.GET.get('username')
    room_details=Room.objects.get(name=room)

    return render(requests,'room.html',{'room_details':room_details,'username':username})


def send(requests):
    message=requests.POST['message']
    username=requests.POST['username']
    room_id=requests.POST['room_id']

    if message=='':
        return HttpResponse('u cant do it')
    else:

        new_message=Message.objects.create(value=message,user=username,room=room_id)
        new_message.save()
        return HttpResponse('message Sent successfully')

def getMessages(requests,room):
    room_details=Room.objects.get(name=room)
    messages=Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def sample(requests):
    return JsonResponse({"name":"hellobhai"})


def about(requests):
    return render(requests,'about.html')