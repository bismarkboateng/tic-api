from rest_framework.routers import SimpleRouter
from . import viewset


router = SimpleRouter()
router.register(r"auth/register", viewset.RegisterViewSet, basename="register")
router.register(r"auth/login", viewset.LoginViewSet, basename="login")


urlpatterns = [
    *router.urls
]
