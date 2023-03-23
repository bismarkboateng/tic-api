from django.urls import path 
from .views import CreateUserAPIView, AuthenticateUser,UserRetrieveUpdateAPIView


urlpatterns = [
    path("create/", CreateUserAPIView.as_view(), name="create_user"),
    path("authenticate/token/", AuthenticateUser.as_view(), name="authenticate_get_token"),
    path("update/", UserRetrieveUpdateAPIView.as_view(), name="update_retrieve")
]
