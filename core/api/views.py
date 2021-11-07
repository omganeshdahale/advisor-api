from rest_framework import generics
from rest_framework.permissions import AllowAny
from ..models import Advisor
from .serializers import AdvisorSerializer


class AdvisorCreateView(generics.CreateAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer
    permission_classes = (AllowAny,)
