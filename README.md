# BFF con Flask

Este proyecto demuestra el patrón Backend for Frontend (BFF) utilizando Flask como intermediario entre un frontend simple y un backend simulado con POSTGRES Server. Se hace la simulación como si hubieran 2 frontend, uno para una página web y otro para una aplicación de celular.

## Estructura

- **Frontend**: Servido con Nginx, muestra una lista de usuarios y permite agregar o quitar usuarios de la base de datos.
- **BFF**: Aplicación Flask que consume la API del backend y expone un endpoint para el frontend.
- **Backend**: POSTGRES Server que simula una API REST con datos de usuarios.

## Uso

1. Clona el repositorio.
2. Ejecuta `docker-compose up`.
3. Accede a `http://localhost` en tu navegador.