import Utilities.SystemUtilities as ut
import Modules.TemplateRoller as o1

def printMenu():
    print('Escoge lo que quieres hacer hoy')
    print('0. Salir')
    print('1. Tirar dados con un molde establecido')

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

        case _:
            print('No se ha encontrado la opción', selection)
            
