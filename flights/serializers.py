from django.shortcuts import render
from .models import Flight, Booking
from rest_framework import serializers

class FlightView(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['id', 'destination', 'time', 'price']

class BookingView(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']