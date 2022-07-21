from django.urls import path
from .views import EventView, EventCalendar
urlpatterns = [

    path('<int:pk>/', EventView, name='event'),
    path('kalendarz/', EventCalendar.as_view(), name='kalendarz'),
]
