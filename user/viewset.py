from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status 

from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class RegisterViewSet(ViewSet):
    http_method_names = ["post"]
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save() 


        refresh = RefreshToken.for_user(user)

        res = {
            "refresh" : str(refresh),
            "access" : str(refresh.access_token)
        }


        return Response({
            "user": serializer.data, 
            "refresh":res["refresh"],
            "access":res["access"]
        }, status=status.HTTP_201_CREATED)
    

class LoginViewSet(ViewSet):
    http_method_names = ["post"]
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )


    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data) 

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        
        return Response(serializer.validate_data, status=status.HTTP_200_OK)