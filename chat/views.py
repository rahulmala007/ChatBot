from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import json
from django.utils.safestring import mark_safe
from .models import Chat, Contact
# Create your views here.


def get_lastest(chatid):
    chat = get_object_or_404(Chat, pk=chatid)
    messages = chat.messages.order_by('-timestamp').all()[:10]
    return messages


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)


def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    # try:
    # 	newchat = Chat.objects.get(slug_url=slug)
    # except RealEstateListing.DoesNotExist:
    # 	newchat = None
    newchat = Chat.objects.create()
    newchat.save()
    chatid = newchat.pk
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        'chatid': mark_safe(json.dumps(chatid))
    })
