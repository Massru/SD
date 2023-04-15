import requests
import json

print('Bienvenido a la página de el hotel')

direccion = "http://localhost:"
puerto = "8090"
servidor = direccion + puerto



menu = '''Elige la opción que desea realizar:
    1. Dar de alta una nueva habitación
    2. Modificar los datos de una habitación
    3. Consultar la lista completa de habitaciones
    4. Consultar una habitación mediante un identificador
    5. Consultar la lista de habitaciones ocupadas o desocupadas
    6. Salir\n'''

print(menu)

opcion = input()

