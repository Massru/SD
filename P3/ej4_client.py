import requests
import json
import sys

print("Bienvenido a la página de la UCA")

direccion = "http://localhost:"
puerto = "8091"
servidor = direccion + puerto

opcion = 0

while opcion != 6:

    menu = '''Elige la opción que desea realizar:
        1. Dar de alta a un nuevo miembro en el directorio
        2. Modificar los datos de un miembro
        3. Consultar la lista de todos los miembros
        4. Hacer una búsqueda por DNI
        5. Consultar los miembros según la categoría
        6. Salir'''
    
    print(menu)

    opcion = 0 #Resetear el valor opcion

while opcion <1 or opcion >6:
    opcion = input()
    opcion = int(opcion)

    if opcion == 1:
        dni = input("introduzca el DNI: ")
        nombre = input("Introduzca el nombre: ")
        correo = input("Introduzca el correo: ")
        departamento = input("Introduzca el departamento: ")
        categoria = input("Introduzca la categoria (PAS/PDI/becario): ")
        asignaturas = input("Introduzca las asignaturas: ")
        response = requests.post(servidor + '/addpersonal', json={"dni": dni, "nombre": nombre, "correo": correo, "departamento": departamento, "categoria": categoria, "asignaturas": asignaturas})
        print("Personal añadido")
    if opcion == 6:
        sys.exit("Adiós")