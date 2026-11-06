
from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),

    path('', views.home, name='home'),

    path('create', views.create_birthday, name='create_birthday'),

    path('link_created/<uuid:uuid>/', views.link_created, name='link_created'),

    path('birthday_cake/<uuid:uuid>/', views.birthday_cake, name='birthday_cake'),

    path('birthday_wish/<uuid:uuid>/', views.birthday_wish, name='birthday_wish'),
]
