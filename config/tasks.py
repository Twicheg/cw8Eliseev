import os

from celery import shared_task
from datetime import datetime
import requests
from habit.models import Habit
from overall.services import get_chat_id
from users.models import User

TOKEN = os.getenv('TG_BOT_TOKEN')
URL = f"https://api.telegram.org/bot{TOKEN}"


@shared_task
def message_send(owner_id, place, action, time, chat_id):
    for i in User.object.all():
        if i.id == owner_id:
            owner = i.email
    param = {
        "chat_id": chat_id,
        "text": f'{owner}, you must do {action} in {place} at {time}'
    }
    requests.get(f'{URL}/sendMessage', params=param)


@shared_task
def check():
    time_now = datetime.now().replace(microsecond=False)
    for obj in Habit.objects.all():
        if obj.last_send:
            if obj.last_send.time() <= time_now.time() and (time_now - obj.last_send.replace(tzinfo=None)).days >= 1:
                if obj.owner.tg_chat_id:
                    message_send.delay(time=obj.time, owner_id=obj.owner.id, place=obj.place, action=obj.action,
                                       chat_id=obj.owner.tg_chat_id)
                else:
                    user_chat_id = get_chat_id(obj.owner.tg_username, obj.owner.id)
                    message_send.delay(time=obj.time, owner_id=obj.owner.id, place=obj.place, action=obj.action,
                                       chat_id=user_chat_id)
                obj.last_send = time_now
                obj.save()

        else:
            if obj.time <= time_now.time():
                if obj.owner.tg_chat_id:
                    message_send.delay(time=obj.time, owner_id=obj.owner.id, place=obj.place, action=obj.action,
                                       chat_id=obj.owner.tg_chat_id)
                else:
                    chat_id = get_chat_id(obj.owner.tg_username, obj.owner.id)
                    message_send.delay(time=obj.time, owner_id=obj.owner.id, place=obj.place, action=obj.action,
                                       chat_id=chat_id)
                obj.last_send = time_now
                obj.save()
