import ordersapp.views as ordersapp
from django.urls import path

app_name="ordersapp"

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='list'),
    path('create/', ordersapp.OrderCreate(), name='create'),
    path('update/<pk>/', ordersapp.OrderUpdate(), name='update'),
    path('delete/<pk>/', ordersapp.OrderDelete(), name='delete'),
    path('read/<pk>/', ordersapp.OrderRead(), name='read'),
    path('forming/complete/<pk>/', ordersapp.forming_complete(), name='forming_complete'),
]