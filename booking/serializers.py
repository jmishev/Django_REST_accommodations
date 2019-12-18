from rest_framework import serializers
from .models import Room, Apartment, Hotel, RoomType, Reservation

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ("number", )


class RoomTypeSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(read_only=True, many=True)

    class Meta:
        model = RoomType
        fields = ("name", "price", "rooms")



class HotelSerializer(serializers.ModelSerializer):
    room_types = RoomTypeSerializer(read_only=True, many=True)

    class Meta:
        model = Hotel
        fields = ("name", "room_types")


class ApartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Apartment
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = "__all__"


class FreeHotelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ("name", "country", "city", "apartment")
