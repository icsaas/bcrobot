from django.contrib import admin
from weixin.models import  User,New,Message

# Register your models here.
admin.site.register(User)
admin.site.register(New)
admin.site.register(Message)