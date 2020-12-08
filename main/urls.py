from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.test,name='test'),
    path('test2',views.test2,name='test2'),
    path('test3',views.test3,name='test3'),
    path('account/signup/',views.CreateUserView.as_view(), name = 'signup'),
    path('login/done',views.RegisteredView.as_view(), name = 'create_user_done'),
    path('account/', include('django.contrib.auth.urls')),
]