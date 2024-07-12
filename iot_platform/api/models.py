from django.utils.timezone import make_aware
from django.utils import timezone
from django.db import models
import datetime
import uuid
import json

class Admin(models.Model):
	username = models.CharField(max_length=255, primary_key=True)
	password = models.CharField(max_length=255)


class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_api_key = models.UUIDField(default=uuid.uuid4, editable=False)


class Location(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	location_name = models.CharField(max_length=255)
	location_country = models.CharField(max_length=255)
	location_city = models.CharField(max_length=255)
	location_meta = models.TextField()


class Sensor(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sensor_name = models.CharField(max_length=255)
    sensor_category = models.CharField(max_length=255)
    sensor_meta = models.TextField()
    sensor_api_key = models.UUIDField(default=uuid.uuid4, editable=False)


class SensorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    data = models.TextField()  # Campo para almacenar el JSON completo
    timestamp = models.DateTimeField()

    # Método para guardar los datos en formato JSON
    def save_data(self, json_data):
        self.data = json.dumps(json_data)
        self.timestamp = timezone.now()
        self.save()

    # Método para obtener los datos en formato JSON
    def get_data(self):
        return json.loads(self.data)

    # Método para obtener la marca de tiempo en formato EPOCH
    def get_timestamp_epoch(self):
        return int(self.timestamp.timestamp())

    # Método estático para convertir EPOCH a DateTime
    @staticmethod
    def epoch_to_datetime(epoch_time):
        return make_aware(datetime.datetime.fromtimestamp(epoch_time))