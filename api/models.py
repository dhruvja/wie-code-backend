from django.db import models
from django.contrib.auth.models import User
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
import random
# Create your models here.

class Document(models.Model):
    user = models.ForeignKey(User, related_name = "document_user", on_delete = models.CASCADE) 
    folder_name = models.CharField(max_length=255)
    document_name = models.CharField(max_length=255)
    document = models.FileField(upload_to = "uploads/")
    encrypted = models.BooleanField(default=False)

    def __str__(self):
        return self.document_name

class UserInfo(models.Model):
    user = models.ForeignKey(User, related_name = "user_info_user", on_delete = models.CASCADE)
    height = models.CharField(max_length = 255)
    weight = models.CharField(max_length = 255)
    allergies = models.TextField(blank=True)
    blood_group = models.CharField(max_length = 255)
    dob = models.CharField(max_length = 255)
    age = models.IntegerField(default = 0)
    gender = models.CharField(max_length = 255)

    def __str__(self):
        return self.allergies

class Track(models.Model):
    user = models.ForeignKey(User, related_name = "track_user", on_delete = models.CASCADE)
    latitude = models.FloatField(blank = True, null=True)
    longitude = models.FloatField(blank = True, null=True)
    ip = models.CharField(max_length = 255)

    def __str__(self):
        return self.latitude
    
class EmergencyContacts(models.Model):
    user = models.ForeignKey(User, related_name = "emergency_user", on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 255)
    relation = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Qr(models.Model):
   user = models.ForeignKey(User, related_name = "qr_user", on_delete = models.CASCADE)
   url=models.CharField(max_length=255)
   image=models.ImageField(upload_to='qrcode',blank=True)

   def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.url)
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.image.save(f'image{random.randint(0,9999)}.png',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)

