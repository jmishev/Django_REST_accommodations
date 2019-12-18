from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("hotel", views.HotelView, base_name="hotel")
router.register("apartment", views.ApartmentView)
router.register("rooms", views.RoomView)
router.register("rooms_types", views.RoomTypeView, base_name="rooms")
router.register("reservation", views.ReservationView, base_name="reservations")
router.register("free", views.FreeHotelView, base_name="accommodation")


urlpatterns = [
    path("", include(router.urls)),
]

