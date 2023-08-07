import random

def rollDice(faces):
    return random.randint(1,faces)

def rollD20():
    return random.randint(1,20)

def readTemplate(template):
    if not template[0].isdigit():
        raise Exception('El patrón debe de empezar por un numero')
    dados = {}
    tempnum = ''
    i = 0
    while i < len(template):
        tempnum = template[i]
        i+=1
        while(i<len(template) and template[i].isdigit()):
            tempnum += template[i]
            i+=1
        print(tempnum)
        if i == len(template):
            if 0 in dados:
                dados[0] = int(tempnum) + dados[0]
            else:
                dados[0] = int(tempnum)
            return dados
        if template[i] == '+':
            if 0 in dados:
                dados[0] = int(tempnum) + dados[0]
            else:
                dados[0] = int(tempnum)
        elif template[i] == 'd':
            i+=1
            if i>=len(template):
                raise Exception('Error, el formato no puede terminar en una d')
            tempDice = template[i]
            i+=1
            while(i<len(template) and template[i].isdigit()):
                tempDice += template[i]
                i+=1
            if int(tempDice) in dados:
                dados[int(tempDice)] = int(tempnum) + dados[int(tempDice)]
            else:
                dados[int(tempDice)] = int(tempnum)
    return dados