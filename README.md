# IoT API con Django REST Framework (DRF)
Este proyecto implementa una API REST para gestionar una plataforma de dispositivos IoT. La API, desarrollada con Django Rest Framework (DRF), permite a las compañías administrar sensores, ubicaciones y los datos recopilados por dichos dispositivos. Además, incluye mecanismos de autenticación mediante claves API y soporte para operaciones CRUD.

## Características principales:
- Registro y autenticación de administradores y compañías.
- Gestión de ubicaciones y sensores IoT.
- Inserción y consulta de datos de sensores con soporte para filtrado por rango de tiempo.
- Seguridad mediante API keys para acceso controlado.

## Endpoints
### Autenticación y gestión de administradores
- `POST /api/v1/admin-register/`: Registra un nuevo administrador. El password se encripta utilizando el algoritmo PBKDF2.

### Gestión de compañías
- `POST /api/v1/company/`: Registra una nueva compañía (requiere autorización de administrador).
- `GET /api/v1/company/`: Obtiene todas las compañías registradas (requiere autorización de administrador).
- `GET /api/v1/company/<int:pk>/`: Obtiene los detalles de una compañía específica (requiere autorización de administrador).

### Gestión de ubicaciones
- `POST /api/v1/location-create/`: Registra una nueva ubicación (requiere autorización de administrador).
- `GET /api/v1/location/`: Obtiene todas las ubicaciones asociadas a una compañía (requiere autorización con `company_api_key`).
- `GET /api/v1/location/<int:pk>/`: Obtiene detalles de una ubicación específica.
- `PUT /api/v1/location/<int:pk>/`: Actualiza detalles de una ubicación específica.
- `DELETE /api/v1/location/<int:pk>/`: Elimina una ubicación.

### Gestión de sensores
- `POST /api/v1/sensor-create/`: Registra un nuevo sensor (requiere autorización de administrador).
- `GET /api/v1/sensor/`: Obtiene todos los sensores asociados a una compañía (requiere autorización con `company_api_key`).
- `GET /api/v1/sensor/<int:pk>/`: Obtiene detalles de un sensor específico.
- `PUT /api/v1/sensor/<int:pk>/`: Actualiza detalles de un sensor.
- `DELETE /api/v1/sensor/<int:pk>/`: Elimina un sensor.

### Gestión de datos de sensores
- `POST /api/v1/sensor-data/`: Inserta datos enviados por un sensor. Requiere validación con `sensor_api_key`.
- `GET /api/v1/sensor-data/`: Obtiene todos los datos registrados por sensores de una compañía. Admite parámetros de filtro:
  - `sensor_id`: IDs de sensores específicos.
  - `from`: Marca de tiempo de inicio (EPOCH).
  - `to`: Marca de tiempo de fin (EPOCH).

## Base de Datos
El proyecto utiliza una base de datos SQLite que sigue el siguiente modelo entidad-relación.

![T3 - Emergentes](https://github.com/user-attachments/assets/d22feb63-a0b0-4cb1-ba2a-dd200beb565e)
