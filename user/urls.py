from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.CreateUserAPIView.as_view(), name="create_user"),
    path("authenticate/", views.authenticate_user, name="authenticate"),
    path("all/", views.ListUserView.as_view(), name="list-users"),
    path("update/", views.UserRetrieveUpdateAPIView.as_view(), name="retrieve-update")
]
