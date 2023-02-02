#define URL route for index() view
from django.urls import path
from . import views
from .views import MenuTitle, MenuItems, MenuPrice, MenuInventory, BookingName, BookingNo_of_guests, BookingBookingDate


urlpatterns = [
    path('menu/', MenuTitle.as_view(), name='menu-title'),
    path('menu/<int:pk>/', MenuItems.as_view(), name='menu-items'),
    path('menu/price/<int:pk>/', MenuPrice.as_view(), name='menu-price'),
    path('menu/inventory/<int:pk>/', MenuInventory.as_view(), name='menu-inventory'),
    path('booking/', BookingName.as_view(), name='booking-name'),
    path('booking/guests/<int:pk>/', BookingNo_of_guests.as_view(), name='booking-guests'),
    path('booking/date/<int:pk>/', BookingBookingDate.as_view(), name='booking-date'),
]