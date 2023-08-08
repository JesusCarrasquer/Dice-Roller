import requests
import json

def startModule():

    # SELECCIÓN DE CLASE
    print('Cargando clases...')
    classesCall = requests.get('https://www.dnd5eapi.co/api/classes').json()['results']
    spellcastingClasses = []
    for checkClass in classesCall:
        className = checkClass['index']
        detailsCall = requests.get('https://www.dnd5eapi.co/api/classes/'+className+'/Spellcasting').status_code
        if detailsCall == 200:
            spellcastingClasses.append(className)
    for i in range (0,len(spellcastingClasses)):
        print(i,'-',spellcastingClasses[i])
    selectedClassInt = input('¿De que clase es el hechizo?\n')
    validated = False
    while not validated:
        try:
            selectedClassInt = int(selectedClassInt)
            if selectedClassInt < 0 or selectedClassInt >= len(spellcastingClasses):
                raise ValueError()
            validated = True
        except ValueError:
            selectedClassInt = input('Error, debes introducir un numero correcto y dentro del rango presentado')
    selectedClass = spellcastingClasses[selectedClassInt]
    
    # SELECCIÓN DE NIVEL
    print('Cargando hechizos...')
    classSpells = requests.get('https://www.dnd5eapi.co/api/classes/'+selectedClass+'/spells').json()['results']
    for spell in range(0,len(classSpells)):
        print(str(spell) + ' - ' + classSpells[spell]['name'])
        
    selectedLevelInt = input('¿Que hechizo quieres tirar?\n ')
    validated = False
    while not validated:
        try:
            selectedLevelInt = int(selectedLevelInt)
            if selectedLevelInt < 0 or selectedLevelInt >= len(classSpells):
                raise ValueError()
            validated = True
        except ValueError:
            selectedLevelInt = input('Error, debes introducir un numero correcto y dentro del rango presentado')
    



    input('Pulsa cualquier boton para continuar...')
