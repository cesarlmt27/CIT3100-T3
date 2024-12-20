from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Location
from api.serializers import LocationSerializer
from api.permissions import is_admin_authorized, is_company_authorized

class CreateLocationView(APIView):
    # Crear una nueva Location (solo para Admin)
    def post(self, request):
        if not is_admin_authorized(request):
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyLocationView(APIView):
    # Método para ver todas las Location de la Company o una Location específica
    def get(self, request, pk=None):
        if not is_company_authorized(request):
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        company_api_key = request.headers.get('company-api-key')
        
        if pk:
            try:
                location = Location.objects.get(pk=pk, company__company_api_key=company_api_key)
                serializer = LocationSerializer(location)
            except Location.DoesNotExist:
                return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            locations = Location.objects.filter(company__company_api_key=company_api_key)
            serializer = LocationSerializer(locations, many=True)
        
        return Response(serializer.data)

    # Actualizar una Location específica de la Company
    def put(self, request, pk):
        if not is_company_authorized(request):
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        company_api_key = request.headers.get('company-api-key')
        try:
            location = Location.objects.get(pk=pk, company__company_api_key=company_api_key)
            serializer = LocationSerializer(location, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Location.DoesNotExist:
            return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)

    # Eliminar una Location específica de la Company
    def delete(self, request, pk):
        if not is_company_authorized(request):
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        
        company_api_key = request.headers.get('company-api-key')
        try:
            location = Location.objects.get(pk=pk, company__company_api_key=company_api_key)
            location.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Location.DoesNotExist:
            return Response({"error": "Location not found"}, status=status.HTTP_404_NOT_FOUND)