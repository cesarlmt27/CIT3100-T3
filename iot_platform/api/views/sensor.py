from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Sensor
from api.serializers import SensorSerializer
from api.permissions import is_admin_authorized, is_company_authorized

class CreateSensorView(APIView):
	# Crear un nuevo Sensor (solo para Admin)
	def post(self, request):
		if not is_admin_authorized(request):
			return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
		serializer = SensorSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanySensorView(APIView):
	# Método para ver todos los Sensor de la Company o un Sensor específico
	def get(self, request, pk=None):
		if not is_company_authorized(request):
			return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
		
		company_api_key = request.headers.get('company-api-key')
		
		if pk:
			try:
				sensor = Sensor.objects.get(pk=pk, location__company__company_api_key=company_api_key)
				serializer = SensorSerializer(sensor)
			except Sensor.DoesNotExist:
				return Response({"error": "Sensor not found"}, status=status.HTTP_404_NOT_FOUND)
		else:
			sensors = Sensor.objects.filter(location__company__company_api_key=company_api_key)
			serializer = SensorSerializer(sensors, many=True)
		
		return Response(serializer.data)

	# Actualizar un Sensor específico de la Company
	def put(self, request, pk):
		if not is_company_authorized(request):
			return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
		
		company_api_key = request.headers.get('company-api-key')
		try:
			sensor = Sensor.objects.get(pk=pk, location__company__company_api_key=company_api_key)
			serializer = SensorSerializer(sensor, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except Sensor.DoesNotExist:
			return Response({"error": "Sensor not found"}, status=status.HTTP_404_NOT_FOUND)

	# Eliminar un Sensor específico de la Company
	def delete(self, request, pk):
		if not is_company_authorized(request):
			return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
		
		company_api_key = request.headers.get('company-api-key')
		try:
			sensor = Sensor.objects.get(pk=pk, location__company__company_api_key=company_api_key)
			sensor.delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		except Sensor.DoesNotExist:
			return Response({"error": "Sensor not found"}, status=status.HTTP_404_NOT_FOUND)