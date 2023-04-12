import json

from bottle import run, request, response, get, put, post

database = dict()

class Room:
    def __init__(self, code, tam, equip, free):
        self.code = code
        self.tam = tam
        self.equip = equip
        self.free = free

@post('/addroom')
def add_room():

    data = request.json

    code = data.get('code')
    tam = data.get('tam')
    equip = data.get('equip')
    free = free.get('free')

    room = Room(code, tam, equip, free)


@get('/listrooms')
def list_rooms():
    rooms = []

    for key, value in database.items():
        rooms.append({'code': key, "name": value.name})