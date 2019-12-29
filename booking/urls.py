from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("hotel", views.HotelView)
router.register("apartment", views.ApartmentView)
router.register("rooms", views.RoomView)
router.register("rooms_types", views.RoomTypeView)
router.register("reservation", views.ReservationView)
router.register("free", views.FreeHotelView, basename="free")


urlpatterns = [
    path("", include(router.urls)),
]

