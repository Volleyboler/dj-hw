from django.urls import path

from .views import SensorsAPIView, RetrieveUpdateSensorAPIView, CreateAPIView


urlpatterns = [
    path('sensor/', SensorsAPIView.as_view()),
    path('sensor_update/', RetrieveUpdateSensorAPIView.as_view()),
]
