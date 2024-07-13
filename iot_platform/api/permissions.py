from .models import Admin, Company

# Método para verificar si el usuario está autorizado
def is_admin_authorized(request):
    username = request.headers.get('username')
    return Admin.objects.filter(username=username).exists()

# Método para verificar si la compañía está autorizada
def is_company_authorized(request):
    company_api_key = request.headers.get('company_api_key')
    return Company.objects.filter(company_api_key=company_api_key).exists()