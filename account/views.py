from dj_rest_auth.views import LogoutView
from rest_framework import generics, permissions
from . import serializers

class UserRegisterView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer

class CastomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)