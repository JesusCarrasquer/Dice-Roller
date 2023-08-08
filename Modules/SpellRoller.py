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
        
        #TIRADA DE ATAQUE
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
            
            #GUARDADO DE TIRADA DE ATAQUE
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
        
    #TIRADA DE DAÑO

    damageDices = None
    if 'damage_at_character_level' in spellDetails['damage']:
        #DAÑO DEPENDIENTE DE NIVEL
        selectedLevelInt = input('¿Que nivel es tu personaje?\n ')
        validated = False
        while not validated:
            try:
                selectedLevelInt = int(selectedLevelInt)
                if selectedLevelInt < 1:
                    raise ValueError()
                validated = True
            except ValueError:
                selectedLevelInt = input('Error, debes introducir un numero correcto y superior a 0')
        leveldamages = spellDetails['damage']['damage_at_character_level']
        maxLevel = 0
        for level in leveldamages:
            if int(level) > maxLevel and int(level) < selectedLevelInt:
                maxLevel = int(level)
            damageDices = leveldamages[str(maxLevel)]

    elif 'damage_at_slot_level' in spellDetails['damage']:
        #DAÑO DEPENDIENTE DE RANURA
        slots = spellDetails['damage']['damage_at_slot_level']
        print(slots)
        selectedSlotInt = input('¿Que ranura usas para el hechizo?\n')
        validated = False
        while not validated:
            try:
                if not selectedSlotInt in slots:
                    raise ValueError()
                validated = True
            except ValueError:
                selectedLevelInt = input('Error, debes introducir una ranura correcta')
        damageDices = slots[str(selectedSlotInt)]
    else:
        print('El hechizo no tiene tiradas de daño')
        input('Presiona enter para continuar...')
        return
    #TIRANDO EL DAÑO
    damageDices = damageDices.replace(" ","")
    damageRoll = dr.readTemplate(damageDices)
    formattedDices = dr.rollDices(damageRoll)
    print('El resultado de los dados es:', formattedDices[0])
    print('Resultado detallado:', formattedDices[1])
    #GUARDADO DE TIRADA DE DAÑO
    save = input('¿Deseas guardar la tirada de daño en memoria para otras ocasiones? (Y/N)\n')
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
