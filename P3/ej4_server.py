import json

from bottle import run, request, response, get, put, post

database = dict()

class Personal:
    def __init__(self, dni, nombre, correo, departamento, categoria, asignaturas):
        self.dni = dni
        self.nombre = nombre
        self.correo = correo
        self.departamento = departamento
        self.categoria = categoria
        self.asignaturas = asignaturas

@get('/listpersonal')
def list_personal():
    personal = dict()

    for key, value in database.items():
        personal.update({"dni": key, "nombre": value.nombre, "correo": value.correo, "departamento": value.departamento, "categoria": value.categoria, "asignaturas": value.asignaturas})

        response.headers['Content-Type'] = 'application/json'

        return json.dumps(personal)
    
@get('/listpersonal/<personal_dni>')
def list_personal(personal_dni):
    personal = dict()

    for key, value in database.items():
        if value.code == personal_dni:
            personal.update({"code": key, "nombre": value.nombre, "correo": value.correo, "departamento": value.departamento, "categoria": value.categoria, "asignaturas": value.asignaturas})

    response.headers['Content-Type'] = 'application/json'

    return json.dumps(personal)
    
@post('/addpersonal')
def add_personal():
    
    data = request.json

    dni = data.get('dni')
    nombre = data.get('nombre')
    correo = data.get('correo')
    departamento = data.get('departamento')
    categoria = data.get('categoria')
    asignaturas = data.get('asignaturas')

    personal = Personal(dni, nombre, correo, departamento, categoria, asignaturas)

    database[dni] = personal

    response.headers['Content-Type'] = 'application/json'

    dict_to_parse = {'dni': dni, 'nombre': nombre, 'correo': correo, 'departamento': departamento, 'categoria': categoria, 'asignaturas': asignaturas}

    return json.dumps(dict_to_parse)

@put('/updatepersonal/<personal_dni>')
def update_personal(personal_dni):

    personal = database[personal_dni]

    response.headers['Content-Type'] = 'application/json'

    new_nombre = request.json.get('nombre')
    personal.nombre = new_nombre
    new_correo = request.json.get('correo')
    personal.correo = new_correo
    new_departamento = request.json.get('departamento')
    personal.departamento = new_departamento
    new_categoria = request.json.get('categoria')
    personal.categoria = new_categoria
    new_asignaturas = request.json.get('asignaturas')
    personal.asignaturas = new_asignaturas

    dict_to_parse = {'dni': personal.dni, 'nombre': personal.nombre, 'correo': personal.correo, 'departamento': personal.departamento, 'categoria': personal.categoria, 'asignaturas': personal.asignaturas}

    return json.dumps(dict_to_parse)

if __name__ == '__main__':

    run(host = 'localhost', port = 8091, debug = True)