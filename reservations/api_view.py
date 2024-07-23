from rest_framework import permissions, viewsets, generics
from .serializers import ReservationSerializer
from .models import Reservation
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.forms.models import model_to_dict

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.AllowAny]


