import requests
import sys

print("Bienvenido a la página de gestion de usuarios")

direccion = "http://localhost/"
puerto = "8092"
servidor = direccion + puerto

opcion = 0

while opcion != 5:

    menu = '''Elige la opción que desea realizar:
        1. Registrar un usuario
        2. Activar una cuenta
        3. Busqueda de usuario
        4. Listar usuarios
        5. Salir'''
    
    print(menu)

    opcion = 0 #Resetear el valor opcion

    while opcion <1 or opcion >5:
        opcion = input()
        opcion = int(opcion)

    if opcion == 1:
        user = input("Introduzca el nombre de usuario:")
        password = input("Introduzca la contraseña: ")
        activate = False
        correo = input("Introduzca el correo: ")
        name = input("Introduzca el nombre completo: ")
        response = requests.post(servidor + '/adduser', json={"user": user, "password": password, "activate": activate, "correo": correo, "name": name})
    if opcion == 2:
        user = input("Introduzca el usuario de la cuenta que quiere activar: ")
        activate = True
        response = requests.put(servidor + '/activate/' + user, json={"activate": activate})
    if opcion == 3:
        cadena = input("Introduce el usuario o el correo: ")
        response = requests.get(servidor + '/listuser/' + cadena)
        print(response.text)
    if opcion == 4:
        response = requests.get(servidor + '/listusers')
        print(response.text)
    if opcion == 5:
        sys.exit("Fin de la conexión")