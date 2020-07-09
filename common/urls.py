from django.urls import path
from common.views import ListCar, index

app_name = 'common'
urlpatterns = [
    path('', index, name="index"),
    path('allcars/', ListCar.as_view(), name='car-list'),
]
