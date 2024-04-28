from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/<int:catid>/', views.categ, name='categ'),
    path('widh',views.widh,name ='widh'),
    path('post/<int:pk>/', views.detail, name ='detail'),
]
