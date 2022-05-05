from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_LocMunca, name='create'),
    # path('search/', views.search, name='search'),
    # path('update/<int:pk>', views.update, name='update'),
    # path('delete/<int:pk>', views.delete, name='delete'),
]