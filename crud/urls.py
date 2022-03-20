from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='home'),
    path('adventurer/', views.create_adventurer, name='add_adventurer'),
    path('adventurer/<str:pk>/', views.detail_adventurer, name='detail_adventurer'),
    path('adventurer_update/<str:pk>/', views.update_adventurer, name='update_adventurer'),
    path('adventurer_delete/<str:pk>/', views.delete_adventurer, name='delete_adventurer'),
    path('img/', views.upload_image, name='upload_image')
]
