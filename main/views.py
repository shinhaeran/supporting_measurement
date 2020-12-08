from django.shortcuts import render
from .models import *
from django.contrib.auth.models import AbstractUser
from .forms import CreateUserForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView,CreateView
from django.urls import reverse_lazy
# Create your views here.
# def test(request): 
#     import pandas as pd
#     a = pd.read_csv('/Users/shinhaeran/Desktop/전국주차장정보표준데이터2.csv',engine='python',encoding='CP949')
#     column_a = a[['위도','경도','제공기관명','소재지지번주소']] # 컬럼 List로 전달
#     result=column_a.dropna(axis=0)#결측값 있는 행 삭제
    
#     for i in range(len(result)):
#         r = result.iloc[i]
#         area = r['소재지지번주소'].split() 
#         try:
#             Data.objects.create(data_type='주차장정보',location = r['소재지지번주소'],Latitude=r['위도'],longitude=r['경도'],area1 = area[0],area2=area[1])
#         except:
#             area = r['소재지지번주소'].split('?') 
#             Data.objects.create(data_type='주차장정보',location = r['소재지지번주소'],Latitude=r['위도'],longitude=r['경도'],area1 = area[0],area2=area[1])
    
#     # queryset  =  Data.objects.all()
#     # queryset.delete()

#     return render(request, 'base.html',{
#     })
def test(request): 
    pass
    return render(request, 'base.html',{
    })

def test2(request): 
    from haversine import haversine
    src_lat,src_lon=float(request.GET['lat']),float(request.GET['lon'])

    datas = Data.objects.filter(area1=request.user.area1,area2=request.user.area2)
    result = []
    for i in range(len(datas)):
        try:
            Cart.objects.get(data=datas[i])
        except:
            dst_lat,dst_lon = float(datas[i].Latitude), float(datas[i].longitude)
            result.append((haversine((src_lat,src_lon), (dst_lat,dst_lon), unit = 'km'),datas[i]))
    result=sorted(result,key=lambda x:x[0])
    
    return render(request, 'temp.html',{'src_lat':src_lat,'src_lon':src_lon,'datas':result[0:10]}) #(lat,lon) , [distance], [near_data_index]

def test3(request):
    cart=request.POST.getlist('result[]')
    
    for d in cart:
        d = int(d)
        # Data.objects.create(data_type='주차장정보',location = r['소재지지번주소'],Latitude=r['위도'],longitude=r['경도'],area1 = area[0],area2=area[1])
        Cart.objects.create(user = request.user, data=Data.objects.get(pk=d),state=False)
    cart=Cart.objects.filter(user=request.user,state=False)
    return render(request, 'cart.html',{'cart':cart
    })



class CreateUserView(CreateView): 
    template_name = 'signup.html'
    form_class =  CreateUserForm
    success_url = reverse_lazy('login')


class RegisteredView(TemplateView):
    template_name = 'signup_done.html'