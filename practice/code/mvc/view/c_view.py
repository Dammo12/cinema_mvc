class View:

    def start(self):
        print('-'*40)
        print('BIENVENIDO AL SISTEMA DE CINEMA'.center(40))
        print('-'*40)

    def start_menu(self):
        print('1.- Login')
        print('2.- Registrarse')

    def opcion(self, num):
        print('Ingrese una opción (1-' + num + '): ', end = '')