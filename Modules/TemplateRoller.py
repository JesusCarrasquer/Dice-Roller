import Utilities.SystemUtilities as ut
import Utilities.DiceRoller as dr

def printHelp():
    ut.clearConsole();
    print('Los patrones de dados siguen el formato ndm, siendo n el numero de dados a tirar\n' +
          'Un ejemplo de esto es el patrón "2d2+3d5+4", el cual sumará los resultados de 2 monedas, 3 dados de 5 caras y un 4 fijo.')
    input('Pulsa enter para continuar...')

def askInput():
    ut.clearConsole()
    return input('Introduce el patrón de dados a tirar o "Help" para una guia:\n ')
            
def startModule():
    template = askInput()
    while(template == 'Help'):
        printHelp()
        template = askInput()
    try:
        dadosTirados = dr.readTemplate(template)
    except Exception as e:
        print(str(e))
    resultados = dr.rollDices(dadosTirados)
    print('El resultado de los dados es:', resultados[0])
    print('Resultado detallado:', resultados[1])

    save = input('¿Deseas guardar la tirada en memoria para otras ocasiones? (Y/N)')
    if save == 'Y' or save == 'y':
        fileDesc = input('Introduce el nombre que le quieres dar a la tirada:')
        exists = True
        fileSave = None
        while exists:
            try:
                fileSave = open('Memory/'+fileDesc+'.txt','x')
                exists = False
            except FileExistsError:
                print('Ya existe una tirada con ese nombre, intenta con otro')
        fileSave.write(template)
        fileSave.close()
        input('Tirada guardada con éxito, presiona enter para continuar')

    
    

