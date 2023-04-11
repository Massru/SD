import json

from bottle import post, request, run

mis_elementos = [1, 2]

@post('/inserta')
def inserta():
    try:
        data = json.load((request.body))
    except:
        raise ValueError
    
    i = 0
    existe = False
    while i < len(mis_elementos):
        if mis_elementos[i] == data['elemento']:
            existe = True
        i += 1

    if existe == False:
        mis_elementos.append(data['elemento'])

    return json.dumps({'mis_elementos': mis_elementos})

run(host='localhost', port=8090)