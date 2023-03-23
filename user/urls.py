from django.urls import path
from . import views

urlpatterns = [
    path("create_user/", views.CreateUserAPIView.as_view(), name="create_user"),
    path("authenticate_user/", views.authenticate_user, name="authenticate"),
    path("list_users/", views.ListUserView.as_view(), name="list-users"),
    path("retrieve_update_user/", views.UserRetrieveUpdateAPIView.as_view(), name="retrieve-update")
]
