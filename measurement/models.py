from django.db import models


class Sensor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True)


class Measurement(models.Model):
    sensor_id = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
