from crudfunc import views
from django.urls import path

urlpatterns = [
    path('add/', views.addOwner),
    path('view/', views.viewOwner),
    path('delete/', views.deleteOwner),
    path('update/', views.updateOwner)
]
