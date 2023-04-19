import json

from bottle import run, request, response, get, put, post

database = dict()

class Usuario:
    def __init__(self, user, password, activate, correo, name):
        self.user = user
        self.password = password
        self.activate = activate
        self.correo = correo
        self.name = name

@post('/adduser')
def adduser():
    data = request.json

    user = data.get('user')
    password = data.get('password')
    activate = data.get('activate')
    correo = data.get('correo')
    name = data.get('name')

    usuario = Usuario(user, password, activate, correo, name)

    database[user] = usuario

    response.headers['Content-Type'] = 'application/json'

    dict_to_parse = {'user': user, 'password': password, 'activate': activate, 'correo': correo, 'name': name}

    return json.dumps(dict_to_parse)

@get('/listuser/<cadena>')
def listuser(cadena):

    user = []

    for key, value in database.items():
        if value.user == cadena or value.correo == cadena:
            user.append({"user": key, "password": value.password, "activate": value.activate, "correo": value.correo, "name": value.name})

    response.headers['content-Type'] = 'application/json'

    return json.dumps(user)

@put('/activate/<user>')
def activate(user):

    usuario = database[user]

    response.headers['Content-Type'] = 'application/json'

    new_activate = request.json.get('activate')
    usuario.activate = new_activate

    dict_to_parse = {'user': usuario.user, 'password': usuario.password, 'activate': usuario.activate, 'correo': usuario.correo, 'name': usuario.name}

    return json.dumps(dict_to_parse)

@get('/listusers')
def listusers():

    users = []

    for key, value in database.items():
        users.append({"user": key, "password": value.password, "activate": value.activate, "correo": value.correo, "name": value.name})

    response.headers['Content-Type'] = 'application/json'

    return json.dumps(users)

if __name__ == '__main__':

    run(host = 'localhost', port = 8092, debug = True)