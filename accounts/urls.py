from django.urls import path
from . import views



urlpatterns=[
    path('',views.home,name='home'),
    path('products/',views.products_list,name='prod'),
    path('customer/<str:pk_test>/',views.customer,name='cus'),
    path('create_order/',views.CreateOrder,name='create_order'),
    path('update_order/<int:pk_update>/',views.UpdateOrder,name='update_order'),
    path('delete_order/<int:pk>/',views.delateOrder,name='delete_order'),
]