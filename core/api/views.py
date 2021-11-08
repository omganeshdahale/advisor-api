from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_datetime
from rest_framework import generics, status
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
        time = request.data.get("time")
        if time is None:
            return Response(
                {"time": ["This field is required."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        time = parse_datetime(time)
        if time is None:
            return Response(
                {"time": ["Enter a valid datetime, use format yyyy-mm-dd hh:mm"]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Booking.objects.create(user=user, advisor=advisor, time=time)
        return Response()


class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user__pk=self.kwargs["user_pk"])
