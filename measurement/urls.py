from django.urls import path

from measurement.views import SensorDetailAPIView, MeasurementAPIView, SensorListCreateAPIView

urlpatterns = [
    path('sensors/<int:pk>/', SensorDetailAPIView.as_view()),
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('measurements/', MeasurementAPIView.as_view())
]
