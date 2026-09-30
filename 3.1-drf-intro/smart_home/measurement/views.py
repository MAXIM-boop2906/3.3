from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import (
    SensorListSerializer,
    SensorDetailSerializer,
    SensorCreateSerializer,
    SensorUpdateSerializer,
    MeasurementCreateSerializer,
)


class SensorListView(generics.ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class SensorDetailView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorCreateView(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorCreateSerializer


class SensorUpdateView(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer


class MeasurementCreateView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer