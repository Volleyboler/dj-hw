from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SensorSerializer, SensorDetailSerializer
from .models import Sensor, Measurement


class SensorsAPIView(ListAPIView):
    sensors = Sensor.objects.all()
    ser = SensorSerializer(sensors, many=True)

    def post(self, request, *args, **kwargs):
        pass


class RetrieveUpdateSensorAPIView(RetrieveUpdateAPIView):
    pass


class CreateAPIView(APIView):
    def get(self, request):

        return Response
