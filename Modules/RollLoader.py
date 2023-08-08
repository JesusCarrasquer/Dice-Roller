import Utilities.SystemUtilities as ut
import Utilities.DiceRoller as dr

def startModule():
    savedRolls = ut.listSaved()
    if len(savedRolls)==0:
        input('No se ha encontrado ninguna tirada guardada, presiona enter para continuar...')
        return
    print('¿Que tirada quieres cargar?')
    for i in range (0,len(savedRolls)):
        print(i,'-',savedRolls[i][:-4])
    selectedRoll = input('Introduce aqui tu selección:')
    try:
        if int(selectedRoll) < 0 or int(selectedRoll) >= len(savedRolls):
            raise ValueError() 
    except ValueError:
        print('Error, debes de introducir un numero correcto y dentro del rango especificado')
        input('Pulsa cualquier boton para continuar...')
        return
    dices = dr.readTemplate(open('./Memory/'+savedRolls[int(selectedRoll)],'r').read())
    resultados = dr.rollDices(dices)
    print('El resultado de los dados es:', resultados[0])
    print('Resultado detallado:', resultados[1])
    input('Pulsa cualquier boton para continuar...')
    