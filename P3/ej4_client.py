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
        dni = input("Introduzca el DNI: ")
        nombre = input("Introduzca el nombre: ")
        correo = input("Introduzca el correo: ")
        departamento = input("Introduzca el departamento: ")
        categoria = input("Introduzca la categoria (PAS/PDI/becario): ")
        asignaturas = input("Introduzca las asignaturas: ")
        response = requests.post(servidor + '/addpersonal', json={"dni": dni, "nombre": nombre, "correo": correo, "departamento": departamento, "categoria": categoria, "asignaturas": asignaturas})
        print("Personal añadido")
    if opcion == 2:
        dni = input("Introduzca dni de personal a editar: ")
        nombre = input("Introduzca el nombre: ")
        correo = input("Introduzca el correo: ")
        departamento = input("Introduzca el departamento: ")
        categoria = input("Introduzca la categoria (PAS/PDI/becario): ")
        asignaturas = input("Introduzca las asignaturas: ")
        response = requests.put(servidor + '/updatepersonal/' + dni, json={"nombre": nombre, "correo": correo, "departamento": departamento, "categoria": categoria, "asignaturas": asignaturas})
        print("Modificación realizada")
    if opcion == 3:
        response = requests.get(servidor + '/listpersonal')
        print(response.text)
    if opcion == 4:
        dni = input("Introduzca el DNI: ")
        response = requests.get(servidor + '/listpersonal/' + dni)
        print(response.text)
    if opcion == 5:
        categoria = input("Introduzca categoria (PAS/PDI/becario): ")
        response = requests.get(servidor + '/listcategoria/' + categoria)
        print(response.text)
    if opcion == 6:
        sys.exit("Fin de la conexión")