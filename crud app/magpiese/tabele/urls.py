from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('create/locmunca', views.create_LocMunca, name='create_locmunca'),
    path('create/anagajati', views.create_Angajat, name='create_angajat'),
    path('search/locurimunca', views.read_LocuriMunca, name='search_locurimunca'),
    path('update/<int:pk>', views.update_LocuriMunca, name='update_locurimunca')
    # path('search/', views.search, name='search'),
    # path('update/<int:pk>', views.update, name='update'),
    # path('delete/<int:pk>', views.delete, name='delete'),
]