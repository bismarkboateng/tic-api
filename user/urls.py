from rest_framework.routers import SimpleRouter
from . import viewset


router = SimpleRouter()
router.register(r"auth/register", viewset.RegisterViewSet, basename="register")

urlpatterns = [
    *router.urls
]
