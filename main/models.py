from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class Group(models.Model):
#     location = models.CharField(max_length=10)      
class CustomUser(AbstractUser):
    group = models.CharField(max_length=10, default='소속없음',blank=True,null=False)
    area1 = models.CharField(max_length=30)
    area2 = models.CharField(max_length=30)
    
  

class Data(models.Model):
    data_type = models.CharField(max_length=10)
    location = models.CharField(max_length=30) #주소
    area1 = models.CharField(max_length=30) # ~시
    area2 = models.CharField(max_length=30) # ~시
    near_view = models.ImageField(null=True, blank=True) #근경
    distant_view = models.ImageField(null=True, blank=True) #원경
    etc =  models.CharField(max_length=30, default='-',blank=True,null=False) #특이사항
    updated_at = models.DateTimeField(auto_now=True) # 실측 날짜
    Latitude = models.CharField(max_length=20) #위도
    longitude = models.CharField(max_length=20) #경도
    
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, default=None, on_delete=models.CASCADE) # cart에 추가한사람 / 완료하면:실측자
    data = models.ForeignKey(Data, default=None, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)#실측 True / False
    