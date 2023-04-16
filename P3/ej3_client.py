import requests
import json
import sys

print('Bienvenido a la página de el hotel')

direccion = "http://localhost:"
puerto = "8090"
servidor = direccion + puerto

opcion = 0

while opcion != 6:

    menu = '''Elige la opción que desea realizar:
        1. Dar de alta una nueva habitación
        2. Modificar los datos de una habitación
        3. Consultar la lista completa de habitaciones
        4. Consultar una habitación mediante un identificador
        5. Consultar la lista de habitaciones ocupadas o desocupadas
        6. Salir'''

    print(menu)

    opcion = 0 #Resetear el valor opcion
    while opcion <1 or opcion >6:
        opcion = input()
        opcion = int(opcion)

    if opcion == 1:
        code = input("Introduzca numero de habitacion nueva: ")
        tam = input("Introduzca el numero de plazas de la habitacion: ")
        equip = input("Introduzca el equipamiento de la habitacion: ")
        free = input("Introduzca si la habitacion está libre (si/no): ")
        response = requests.post(servidor + '/addroom', json={"code": code, "tam": tam, "equip": equip, "free": free})
        print("Habitación añadida")
    if opcion == 2:
        code = input("Introduzca numero de habitacion a editar: ")
        tam = input("Introduzca el numero de plazas de la habitacion: ")
        equip = input("Introduzca el equipamiento de la habitacion: ")
        free = input("Introduzca si la habitacion está libre (si/no): ")
        response = requests.put(servidor + '/updateroom/' + code, json={"tam": tam, "equip": equip, "free": free})
        print("Modificación realizada")
    if opcion == 3:
        response = requests.get(servidor + '/listrooms')
        print("")
        print(response.text)
    if opcion == 4:
        code = input("Identificador de la habitacion: ")
        response = requests.get(servidor + '/listroom/' + code)
        print("")
        print(response.text)
    if opcion == 5:
        free = input("Desea buscar habitaciones libres (si/no): ")
        response = requests.get(servidor + '/listisfree/' + free)
        print("")
        print(response.text)
    if opcion == 6:
        sys.exit("Adiós")