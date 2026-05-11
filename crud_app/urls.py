from django.urls import path
from crud_app import views
urlpatterns=[
    path('', views.home, name='home'),
    path('view/', views.view_data, name='view'),
    path('edit/<int:id>/', views.edit_data, name='edit'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
]