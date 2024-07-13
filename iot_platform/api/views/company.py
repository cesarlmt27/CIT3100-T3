from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Company
from api.serializers import CompanySerializer
from api.permissions import is_admin_authorized

# Vista para crear y obtener Company
class CompanyView(APIView):
    # Método para crear una nueva Company
    def post(self, request):
        if not is_admin_authorized(request):
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Método para ver todas las Company o una Company específica
    def get(self, request, pk=None):
        if not is_admin_authorized(request):
            return Response({"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)
        if pk:
            try:
                company = Company.objects.get(pk=pk)
            except Company.DoesNotExist:
                return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = CompanySerializer(company)
        else:
            # Obtener todas las Companies
            companies = Company.objects.all()
            serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)