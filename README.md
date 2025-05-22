# Backend - Prueba Técnica

Este proyecto es una API REST construida con Django y Django REST Framework para la gestión de empresas, productos y precios en diferentes monedas.

## Estructura principal
- **Empresas**: CRUD completo, solo administradores pueden crear, editar o eliminar.
- **Productos**: CRUD completo, asociados a empresas.
- **Precios**: Cada producto puede tener precios en varias monedas.
- **Usuarios**: Dos tipos: Administrador (gestiona todo) y Externo (solo lectura).
- **Autenticación**: JWT (JSON Web Token).

## Requisitos
- Python 3.10+
- pip
- Docker y Docker Compose (opcional pero recomendado)


## Variables de entorno
Debes crear un archivo `.env` en la **raíz del proyecto** con las variables necesarias para la base de datos, credenciales y otros secretos. Ejemplo:

```
SECRET_KEY=tu_clave_secreta
DB_NAME=nombre_db
DB_USER=usuario_db
DB_PASSWORD=contraseña_db
DB_HOST=localhost
DB_PORT=5432
APP_EMAIL=admin@admin.com
APP_PASSWORD=admin123
```

## Instalación y ejecución

### Opción 1: Usando Docker Compose
1. Asegúrate de tener Docker y Docker Compose instalados.
2. En la raíz del proyecto ejecuta:
   ```powershell
   docker compose -f .\docker-compose.yml --env-file .\.env up --build
   ```
3. El backend estará disponible en `http://localhost:3000/`


## Endpoints principales
- `/api/companies/` CRUD de empresas
- `/api/products/` CRUD de productos
- `/api/products/<id>/prices/` Precios de un producto
- `/api/login/` Login con JWT

## Notas
- El usuario administrador puede gestionar empresas y productos. El usuario externo solo puede consultar.
- El archivo `.env` debe estar en la raíz del proyecto para que tanto Docker como Django lo detecten correctamente.
- Puedes personalizar las variables de entorno según tu entorno local o de despliegue.
