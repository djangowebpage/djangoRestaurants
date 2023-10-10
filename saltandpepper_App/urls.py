from django.urls import path
from . import views
app_name = 'saltandpepper_App'
urlpatterns=[
    path('',views.index,name='index'),

    path('pizza',views.pizza,name='pizza'),
    path('burger',views.burger,name='burger'),
    path('order',views.order,name='order'),
    path('success',views.success,name='success'),
]