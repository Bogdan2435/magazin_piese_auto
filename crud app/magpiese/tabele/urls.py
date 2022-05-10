from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('create/locmunca', views.create_LocMunca, name='create_locmunca'),
    path('create/anagajati', views.create_Angajat, name='create_angajat'),
    path('create/clienti', views.create_Client, name='create_client'),
    path('search/', views.search, name='search'),
    path('search/locurimunca', views.read_LocuriMunca, name='search_locurimunca'),
    path('search/angajati', views.read_Angajati, name='search_angajati'),
    path('update/locurimunca/<int:pk>', views.update_LocuriMunca, name='update_locurimunca'),
    path('update/angajati/<int:pk>', views.update_Angajati, name='update_locurimunca'),
    path('delete/locurimunca/<int:pk>', views.delete_LocuriMunca, name='delete_locurimunca'),
    path('delete/angajati/<int:pk>', views.delete_Angajati, name='delete_angajati'),
    # path('search/', views.search, name='search'),
    # path('update/<int:pk>', views.update, name='update'),
    # path('delete/<int:pk>', views.delete, name='delete'),
]