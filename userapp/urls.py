from userapp import views
from userapp.views import BaseRegisterView, DeleteUser, DetailUser, UpdateUser, UserLoginView, ViewUser
from django.urls import path, include


urlpatterns = [
    path('user-registration/', BaseRegisterView.as_view(), name = "user_registration"),
    path('user-login/', UserLoginView.as_view(), name = "user_login"),
    path('index/', views.index, name= "index"),
    path('view/', ViewUser.as_view(), name = "view_user"),
    path('<int:pk>/detail/', DetailUser.as_view(), name = "detail_user"),
    path('<int:pk>/delete/', DeleteUser.as_view(), name = "delete_user"),
    path('<int:pk>/update/', UpdateUser.as_view(), name = "update_user"),

]
