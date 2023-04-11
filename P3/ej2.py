import json

from bottle import post, request, run

mis_elementos = [1, 2]

@post('/inserta')
def inserta():
    try:
        data = json.load((request.body))
        print(data)
    except:
        raise ValueError
    
    i = 0
    existe = False
    while i < len(mis_elementos):
        if mis_elementos[i] == data['elemento']:
            existe = True
        i += 1

    print(mis_elementos)
    
    if existe == True:
        return json.dumps({'mis_elementos': mis_elementos})
    else:
        mis_elementos.append(data['elemento'])
        return json.dumps(mis_elementos + {'elemento': data['elemento']})

run(host='localhost', port=8090)