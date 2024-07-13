from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import AdminSerializer
from django.contrib.auth.hashers import make_password

# Vista para registrar un Admin
class AdminRegister(APIView):
    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)