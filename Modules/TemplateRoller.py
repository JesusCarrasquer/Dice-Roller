import Utilities.SystemUtilities as ut

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
