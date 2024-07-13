from rest_framework import serializers
from .models import Admin, Company, Location, Sensor, SensorData

class AdminSerializer(serializers.ModelSerializer):
	class Meta:
		model = Admin
		fields = '__all__'

	def to_representation(self, instance):
		# Llamar al método to_representation del padre para obtener el diccionario original
		ret = super().to_representation(instance)
		# Eliminar el campo "password" del diccionario
		ret.pop('password', None)
		# Retornar el diccionario modificado
		return ret


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sensor
		fields = '__all__'


class SensorDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = SensorData
		fields = '__all__'