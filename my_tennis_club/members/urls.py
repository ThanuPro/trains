from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL de la page d'accueil
    path('show_train/<int:train_id>/', views.show_train, name='show_train')
]
