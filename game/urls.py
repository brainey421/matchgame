from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:party_id>/', views.lobby, name='lobby')
]
