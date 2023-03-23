from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User
import jwt 
from django.conf import settings
# from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
from rest_framework.generics import RetrieveUpdateAPIView



class CreateUserAPIView(APIView):
    permission_classes = (AllowAny, )
    
    def post(self, request):
        user = request.data 
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class ListUserView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

# class AuthenticateUser(APIView):
#     permission_classes = (AllowAny,)


#     def post(self, request):
#         try:
#             email = request.data["email"]
#             password = request.data["password"]

#             user = User.objects.get(email=email, password=password)

#             if user: 
#                 try:
#                     payload = jwt.payload_handler(user)
#                     token = jwt.encode(payload, settings.SECRET_KEY)
#                     user_details = {}
#                     user_details["name"] = "%s %s" % (user.first_nme, user.last_name)
#                     user_details["token"] = token 
#                     user.logged_in.send(sender=user.__class__, request=request, user=user)

#                     return Response(user_details, status=status.HTTP_200_OK)
                
#                 except Exception as e:
#                     raise e 
#             else:
#                 res = {
#                     "error":"cannot authenticate with the given credentials"
#                 }
#                 return Response(res, status=status.HTTP_403_FORBIDDEN)
#         except KeyError:
#             res = {"error" : "please provide an email and a password!"}
#             return Response(res)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        email = request.data['email']
        password = request.data['password']
        user = User.objects.get(email=email, password=password)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = "%s %s" % (
                    user.first_name, user.last_name)
                user_details['token'] = token
                # user.logged_in.send(sender=user.__class__,
                #                     request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)
    


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, ) 
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get("user", {})
        serializer = UserSerializer(request.user, data=serializer_data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)