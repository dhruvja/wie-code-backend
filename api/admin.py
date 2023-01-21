from django.contrib import admin
from .models import Document, Qr, UserInfo, Track, EmergencyContacts 

# Register your models here.

admin.site.register(Document)
admin.site.register(Qr)
admin.site.register(UserInfo)
admin.site.register(EmergencyContacts)
admin.site.register(Track)

