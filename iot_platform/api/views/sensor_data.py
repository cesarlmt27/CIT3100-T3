from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from api.models import Sensor, SensorData
from django.utils.timezone import make_aware
import datetime
from api.permissions import is_company_authorized

class SensorDataView(APIView):
	# Método para crear datos de sensores
	def post(self, request):
		api_key = request.data.get('api_key')
		json_data = request.data.get('json_data')
		
		try:
			sensor = Sensor.objects.get(sensor_api_key=api_key)
		except Sensor.DoesNotExist:
			return JsonResponse({'error': 'Invalid sensor_api_key'}, status=status.HTTP_400_BAD_REQUEST)
		
		for data in json_data:
			sensor_data = SensorData(sensor=sensor)
			sensor_data.save_data(data)
		
		return JsonResponse({'message': 'Data created'}, status=status.HTTP_201_CREATED)

	# Método para obtener datos de sensores por Company y rango de tiempo
	def get(self, request):
		if not is_company_authorized(request):
			return JsonResponse({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
		
		sensor_id = request.query_params.getlist('sensor_id')
		from_epoch = request.query_params.get('from')
		to_epoch = request.query_params.get('to')
		
		company_api_key = request.headers.get('company_api_key')
		sensors = Sensor.objects.filter(location__company__company_api_key=company_api_key)
		if sensor_id:
			sensors = sensors.filter(id__in=sensor_id)
		
		sensor_data = SensorData.objects.filter(sensor__in=sensors)
		
		if from_epoch and to_epoch:
			from_datetime = make_aware(datetime.datetime.fromtimestamp(int(from_epoch)))
			to_datetime = make_aware(datetime.datetime.fromtimestamp(int(to_epoch)))
			sensor_data = sensor_data.filter(timestamp__range=(from_datetime, to_datetime))
		
		data = [{'sensor_id': sd.sensor.id, 'data': sd.data, 'timestamp': sd.timestamp} for sd in sensor_data]
		return JsonResponse(data, safe=False, status=status.HTTP_200_OK)