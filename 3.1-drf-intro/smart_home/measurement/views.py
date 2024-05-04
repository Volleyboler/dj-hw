from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorsSerializer
from .models import Sensor, Measurement


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorsListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
