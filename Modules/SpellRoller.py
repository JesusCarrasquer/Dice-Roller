import requests
import json

def startModule():
    print('Cargando clases...')
    classesCall = requests.get('https://www.dnd5eapi.co/api/classes').json()['results']
    spellcastingClasses = []
    for checkClass in classesCall:
        className = checkClass['index']
        detailsCall = requests.get('https://www.dnd5eapi.co/api/classes/'+className+'/Spellcasting').status_code
        if detailsCall == 200:
            spellcastingClasses.append(className)
    print('¿De que clase es el hechizo?')
    for i in range (0,len(spellcastingClasses)):
        print(i,'-',spellcastingClasses[i])
    input('Pulsa cualquier boton para continuar...')
