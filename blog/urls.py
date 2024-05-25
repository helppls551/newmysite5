from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_info, name='post_info'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/notebook/',views.notebook,name='post_notebook'),
    path('post/<pk>/publish',views.publish,name='publish')
]

