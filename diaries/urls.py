from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('work/', views.work, name="work"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('poetries/', views.poetries, name="poetries"),
    path('shayries/', views.shayries, name="shayries"),
    path('oneliner/', views.oneliner, name="oneliner"),
    path('poetries/poeme/<str:pk>', views.poeme, name="poeme"),
    path('shayries/shayrees/<str:sk>', views.shayrees, name="shayrees"),
    path('oneliner/onelines/<str:ok>', views.onelines, name="onelines"),
]
