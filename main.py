import Utilities.SystemUtilities as ut
import Modules.TemplateRoller as o1
import Modules.RollLoader as o2
import Modules.SpellRoller as o3

def printMenu():
    print('Escoge lo que quieres hacer hoy')
    print('0. Salir')
    print('1. Tirar dados con un molde establecido')
    print('2. Cargar tirada guardada')
    print('3. Usar un hechizo de 5e')

game = True
while(game):
    ut.clearConsole()
    printMenu()
    selection = input('Introduce aquí tu elección -> ')
    validated = False
    while(not validated):
        try:
            selection = int(selection)
            validated = True
        except:
            print('Error, debes de introducir un numero...')
            selection = input('Introduce aquí tu elección -> ')
    match selection:
        case 0:
            print('Saliendo del programa...')
            ut.stopProgram()
        case 1:
            o1.startModule()
        case 2:
            o2.startModule()
        case 3:
            o3.startModule()
        case _:
            input('No se ha encontrado la opción ' + str(selection) + ', Pulsa enter para continuar...')
            
