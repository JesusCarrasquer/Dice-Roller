import requests
import json
import Utilities.DiceRoller as dr

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
    
    # SELECCIÓN DE HECHIZO
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
            selectedLevelInt = input('Error, debes introducir un numero correcto y dentro del rango presentado, prueba de nuevo')
    
    #TIRADAS DEL HECHIZO
    spellDetails = requests.get('https://www.dnd5eapi.co/api/spells/'+classSpells[selectedLevelInt]['index']).json()
    if 'attack_type' in spellDetails:
        validated = False
        attackCheck = input('¿Deseas hacer tirada de ataque? (Y/N)\n')
        while not validated:
            try:
                if attackCheck!='n' and attackCheck!='N' and attackCheck!='y' and attackCheck!='Y':
                    raise ValueError()
                validated = True
            except ValueError:
                attackCheck = input('Error, debes introducir "Y" para tirar ataque o "N" para tirar daño directamente\n')
        if attackCheck == 'y' or attackCheck == 'Y':
            spellModifier = input('¿Cual es tu modificador de ataque de hechizo?\n')
            validated = False
            while not validated:
                try:
                    spellModifier = int(spellModifier)
                    validated = True
                except ValueError:
                    spellModifier = input('Error, debes introducir un numero\n')
            attackRoll = dr.rollD20()
            if attackRoll == 1:
                print('¡Vaya pifia! Has sacado un 1 en el ataque, sumando el modificador se obtiene una tirada de ' + spellModifier+1)
            elif attackRoll == 20:
                print('¡Critico! Has sacado un 20 natural, para un total de ' + str(spellModifier+20) + ' tras synar el modificador')
            else:
                print('Tu tirada de ataque ha salido ' + str(attackRoll) + ', sumandole el modificador se obtiene ' + str(attackRoll+spellModifier))
            
            save = input('¿Deseas guardar la tirada en memoria para otras ocasiones? (Y/N)\n')
            if save == 'Y' or save == 'y':
                fileDesc = input('Introduce el nombre que le quieres dar a la tirada: ')
                exists = True
                fileSave = None
                while exists:
                    try:
                        fileSave = open('Memory/'+fileDesc+'.txt','x')
                        exists = False
                    except FileExistsError:
                        print('Ya existe una tirada con ese nombre, intenta con otro')
                fileSave.write('1d20+' + str(spellModifier))
                fileSave.close()
                print('Tirada guardada con exito')
        




    input('Pulsa cualquier boton para continuar...')
