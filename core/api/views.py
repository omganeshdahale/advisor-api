from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Advisor, Booking
from .serializers import UserSerializer, AdvisorSerializer, BookingSerializer

User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer


class AdvisorCreateView(generics.CreateAPIView):
    model = Advisor
    serializer_class = AdvisorSerializer


class AdvisorListView(generics.ListAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer


class BookingCreateView(APIView):
    def post(self, request, user_pk, advisor_pk, format=None):
        user = get_object_or_404(User, pk=user_pk)
        advisor = get_object_or_404(Advisor, pk=advisor_pk)
        Booking.objects.create(user=user, advisor=advisor, time=request.data["time"])
        return Response()


class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user__pk=self.kwargs["user_pk"])
