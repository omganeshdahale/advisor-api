from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny
from ..models import Advisor
from .serializers import UserSerializer, AdvisorSerializer


class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class AdvisorCreateView(generics.CreateAPIView):
    model = Advisor
    serializer_class = AdvisorSerializer
    permission_classes = (AllowAny,)


class AdvisorListView(generics.ListAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
