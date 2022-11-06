from django.db import models
from django.forms import fields


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return 'Датчик' + self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.FloatField()
    image = fields.ImageField(max_length=300, allow_empty_file=True)
    created_at = models.DateTimeField(auto_now_add=True)
