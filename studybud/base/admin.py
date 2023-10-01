from django.contrib import admin

# Register your models here.

from .models import Topic, Room, Message

admin.site.register(Topic)
admin.site.register(Room)
admin.site.register(Message)