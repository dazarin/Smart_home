# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from django.forms import model_to_dict
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from .models import Measurement, Sensor
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorListCreateAPIView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailAPIView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementAPIView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        sensor_id = Sensor.objects.get(id=int(request.data['sensor_id']))
        measurement_new = Measurement.objects.create(
            sensor_id=sensor_id,
            value=request.data['value']
        )
        return Response({'post': model_to_dict(measurement_new)})
