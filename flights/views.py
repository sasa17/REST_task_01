from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import *
from datetime import date

class FlightView(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightView

class BookingView(ListAPIView):
	queryset = Booking.objects.filter(date__gte=date.today())
	serializer_class = BookingView
