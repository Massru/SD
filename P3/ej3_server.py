import json

from bottle import run, request, response, get, put, post

database = dict()

class Room:
    def __init__(self, code, tam, equip, free):
        self.code = code
        self.tam = tam
        self.equip = equip
        self.free = free


@get('/listrooms')
def list_rooms():
    rooms = []

    for key, value in database.items():
        rooms.append({'code': key, "tam": value.tam, "equip": value.equip, "free": value.free})

    response.headers['Content-Type'] = 'application/json'

    return json.dumps(rooms)

@get('/listroom/<room_code>')
def list_room(room_code):
    room = []

    for key, value in database.items():
        if value.code == room_code:
            room.append({'code': key, "tam": value.tam, "equip": value.equip, "free": value.free})
    
    response.headers['Content-Type'] = 'application/json'

    return json.dumps(room)

@get('/listisfree/<room_status>')
def list_room(room_status):
    room = []

    for key, value in database.items():
        if value.free == room_status:
            room.append({'code': key, "tam": value.tam, "equip": value.equip, "free": value.free})
    
    response.headers['Content-Type'] = 'application/json'

    return json.dumps(room)


@post('/addroom')
def add_room():

    data = request.json

    code = data.get('code')
    tam = data.get('tam')
    equip = data.get('equip')
    free = data.get('free')

    room = Room(code, tam, equip, free)

    database[code] = room

    response.headers['Content-Type'] = 'application/json'

    dict_to_parse = {'code': code, 'tam': tam, 'equip': equip, 'free': free}

    return json.dumps(dict_to_parse)

@put('/updateroom/<room_code>')
def update_room(room_code):

    room = database[room_code]

    response.headers['Content-Type'] = 'application/json'

    new_tam = request.json.get('tam')
    room.tam = new_tam
    new_equip = request.json.get('equip')
    room.equip = new_equip
    new_free = request.json.get('free')
    room.free = new_free

    dict_to_parse = {'code': room_code, 'tam': room.tam, 'equip': room.equip, 'free': room.free}

    return json.dumps(dict_to_parse)

if __name__ == '__main__':

    run(host = 'localhost', port = 8090, debug = True)

