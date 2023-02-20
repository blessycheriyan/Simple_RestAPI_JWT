from django.urls import path
from . import views
urlpatterns = [
    path("api/user/signup/", views.SignupAPIView.as_view(), name="user-signup"),
    path("hello", views.hello, name="hello"),
    path("api/user/login/", views.LoginAPIView.as_view(), name="user-login"),
    path("api/students/", views.StudentAPIView.as_view(), name="api-student"),
    
]
  