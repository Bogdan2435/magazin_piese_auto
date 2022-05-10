from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('create/locmunca', views.create_LocMunca, name='create_locmunca'),
    path('create/anagajati', views.create_Angajat, name='create_angajat'),
    path('search/', views.search, name='search'),
    path('search/locurimunca', views.read_LocuriMunca, name='search_locurimunca'),
    path('update/<int:pk>', views.update_LocuriMunca, name='update_locurimunca'),
    path('delete/<int:pk>', views.delete_LocuriMunca, name='delete_locurimunca')
    # path('search/', views.search, name='search'),
    # path('update/<int:pk>', views.update, name='update'),
    # path('delete/<int:pk>', views.delete, name='delete'),
]