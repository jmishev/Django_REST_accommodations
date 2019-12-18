from rest_framework import viewsets
from .models import Apartment, Hotel, Room, RoomType, Reservation
from .serializers import ApartmentSerializer, RoomSerializer, RoomTypeSerializer, \
    ReservationSerializer, HotelSerializer
from django.db.models import Q
from drf_multiple_model.viewsets import ObjectMultipleModelAPIViewSet

class RoomView(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomTypeView(viewsets.ModelViewSet):
    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()


class HotelView(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()


class ApartmentView(viewsets.ModelViewSet):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()

class ReservationView(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()


class FreeHotelView(ObjectMultipleModelAPIViewSet):
    querylist = [
        {'queryset': Hotel.objects.all().prefetch_related("room_types", "room_types__rooms")
            .filter(Q(room_types__rooms__reservation__check_in__lt="2018-01-09") |
                    Q(room_types__rooms__reservation__check_in__isnull=True)),
         'serializer_class': HotelSerializer},
        {'queryset': Apartment.objects.all().select_related()
            .filter(Q(reservation__check_in__lt="2021-01-09") |
                    Q(reservation__check_in__isnull=True)).order_by("price"),
         'serializer_class': ApartmentSerializer},
    ]
