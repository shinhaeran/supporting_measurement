from django.urls import path,include
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.test,name='test'),
    path('test2',views.test2,name='test2'),
    path('cart',views.test3,name='cart'),
    # path('delete/<int:pk>',views.DeleteCart.as_view(), name = 'delete'),
    path('delete/<int:pk>',views.delete_cart, name = 'delete'),
    path('complete/<int:pk>',views.complete, name = 'complete'),
    path('completed/',views.completed_data, name = 'completed'),

    path('account/signup/',views.CreateUserView.as_view(), name = 'signup'),
    path('login/done',views.RegisteredView.as_view(), name = 'create_user_done'),
    path('account/', include('django.contrib.auth.urls')),
]