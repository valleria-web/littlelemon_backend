#define URL route for index() view
from django.urls import path
from . import views
from .views import MenuTitle, MenuPrice, MenuInventory, BookingName, BookingNo_of_guests, BookingBookingDate


urlpatterns = [
    path('menus/', MenuTitle.as_view(), name='menu-title'),
    path('menus/price/<int:pk>/', MenuPrice.as_view(), name='menu-price'),
    path('menus/inventory/<int:pk>/', MenuInventory.as_view(), name='menu-inventory'),
    path('bookings/', BookingName.as_view(), name='booking-name'),
    path('bookings/guests/<int:pk>/', BookingNo_of_guests.as_view(), name='booking-guests'),
    path('bookings/date/<int:pk>/', BookingBookingDate.as_view(), name='booking-date'),
]