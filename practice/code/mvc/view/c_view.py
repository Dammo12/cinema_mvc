class View:

    def start(self):
        print('-'*40)
        print('BIENVENIDO AL SISTEMA DE CINEMA'.center(40))
        print('-'*40)

    def start_menu(self):
        print('1.- Login')
        print('2.- Registrarse')
        print('3.- Salir')

    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def reg_menu(self):
        print('1.- Usuario')
        print('2.- Administrador')
        print('3.- Regresar')

    def opcion(self, num):
        print('Ingrese una opción (1-' + num + '): ', end = '')

    def not_valid_op(self):
        print('-'*40)
        print('¡ Opcion no valida !'.center(40))
        print('-'*40)

    def header(self, msg):
        print('-'*40)
        print(msg.center(40))
        print('-'*40)

    def valid_op(self, msg):
        print('*'*40)
        print(msg.center(40))
        print('*'*40)

    def error(self, msg):
        print('-'*40)
        print('¡ ERROR !'.center(40))
        print(('¡ ' + msg + ' !').center(40))
        print('-'*40)


    #MENU

    def u_menu(self, name):
        print('Bienvenido ' + name + ':')
        print('1.- Comprar boletos')
        print('2.- Ver boletos adquiridos')
        print('3.- Ver horarios de peliculas')
        print('4.- Buscar horarios por pelicula')
        print('5.- Buscar horarios por día')
        print('6.- Regresar')

    def a_menu(self, name):
        print('Administrador ' + name + ':')
        print('1.- Salas')
        print('2.- Asientos')
        print('3.- Peliculas')
        print('4.- Horarios')
        print('5.- Administradores')
        print('6.- Regresar')

    def halls_menu(self):
        print('1.- Agregar nueva sala')
        print('2.- Ver lista de salas')
        print('3.- Editar sala')
        print('4.- Borrar sala')
        print('5.- Regresar')

    def movies_menu(self):
        print('1.- Agregar nueva pelicula')
        print('2.- Ver lista de peliculas')
        print('3.- Ver pelicula')
        print('4.- Editar pelicula')
        print('5.- Borrar pelicula')
        print('6.- Regresar')

    def schedule_menu(self):
        print('1.- Agregar nuevo horario')
        print('2.- Agregar horario a pelicula')
        print('3.- Ver horarios')
        print('4.- Ver horarios de pelicula')
        print('5.- Editar horario')
        print('6.- Borrar horario')
        print('7.- Regresar')

    def admins_menu(self):
        print('1.- Lista Usuarios')
        print('2.- Lista Administradores')
        print('3.- Todas las cuentas')
        print('4.- Cambiar privilegios')
        print('5.- Regresar')

    

    #PRINTS

    def show_movies(self, movies):
        print('='*73)
        print('PELICULAS'.center(73))
        print('='*73)
        print('No:'.ljust(6)+'Pelicula:'.ljust(30)+'Duracion:'.ljust(12)+'Dia inicio:'.ljust(12)+'Dia final:'.ljust(12))
        print('='*73)
        for r in movies:
            print(f'{r[0]:<6}{r[1]:<30}{str(r[2]):<12}{str(r[3]):<12}{str(r[4]):<12}')
        print('='*73)

    def show_movie(self, movie):
        print('='*35)
        print('PELICULA'.center(35))
        print('='*35)
        print('Pelicula: '.ljust(13) + movie[1])
        print('Duracion: '.ljust(13) + str(movie[2]))
        print('Dia inicio: '.ljust(13) + str(movie[3]))
        print('Dia final: '.ljust(13) + str(movie[4]))
        print('='*35)


    
    def show_halls(self, halls):
        print('='*36)
        print('SALAS'.center(36))
        print('='*36)
        print('Sala:'.ljust(6)+'Tipo:'.ljust(10)+'Precio:'.ljust(10)+'Asientos:'.ljust(10))
        print('='*36)
        for r in halls:
            print(f'{r[0]:<6}{r[1]:<10}${r[2]:<10}{r[3]:<10}')
        print('='*36)

    def show_hall(self, hall):
        print('='*35)
        print('SALA'.center(35))
        print('='*35)
        print('Sala: '.ljust(12) + str(hall[0]))
        print('Tipo: '.ljust(12) + hall[1])
        print('Precio: '.ljust(12) + str(hall[2]))
        print('Asientos: '.ljust(12) + str(hall[3]))
        print('='*35)



    
    def show_schedules(self, schedules):
        print('='*29)
        print('HORARIOS'.center(29))
        print('='*29)
        print('No:'.ljust(6)+'Hora:'.ljust(12)+'Día:'.ljust(11))
        print('='*29)
        for r in schedules:
            print(f'{r[0]:<6}{str(r[1]):<12}{str(r[2]):<11}')
        print('='*29)

    def show_schedule(self, schedule):
        print('='*35)
        print('HORARIO'.center(35))
        print('='*35)
        print('No: '.ljust(12) + str(schedule[0]))
        print('Hora: '.ljust(12) + str(schedule[1]))
        print('Dia: '.ljust(12) + str(schedule[2]))
        print('='*35)

    def show_sch_data(self, sch_data):
        print('='*80)
        print('HORARIOS PELICULA'.center(80))
        print('='*80)
        print('No:'.ljust(5)+'Titulo:'.ljust(30)+'Hora:'.ljust(11)+'Día:'.ljust(13)+'Formato:'.ljust(12)+'Precio:'.ljust(9))
        print('='*80)
        for r in sch_data:
            print(f'{str(r[0]):<5}{r[1]:<30}{str(r[2]):<11}{str(r[3]):<13}{r[4]:<12}${str(r[5]):<8}')
        print('='*80)


    def show_users(self, users, msg):
        print('='*75)
        print(('CUENTAS ' + msg).center(75))
        print('='*75)
        print('No:'.ljust(5)+'Nombre:'.ljust(25)+'Correo:'.ljust(45))
        print('='*75)
        for r in users:
            print(f'{r[0]:<5}{r[3]:<25}{r[1]:<45}')
        print('='*75)

    def show_accs(self, users):
        print('='*85)
        print(('CUENTAS').center(85))
        print('='*85)
        print('No:'.ljust(5)+'Nombre:'.ljust(25)+'Correo:'.ljust(45)+'Admin:'.ljust(10))
        print('='*85)
        for r in users:
            print(f'{r[0]:<5}{r[3]:<25}{r[1]:<45}{r[4]:<10}')
        print('='*85)

    def show_acc(self, user):
        print('='*35)
        print('CUENTA'.center(35))
        print('='*35)
        print('No: '.ljust(12) + str(user[0]))
        print('Nombre: '.ljust(12) + user[3])
        print('Correo: '.ljust(12) + user[1])
        print('='*35)

    
    def seats_available(self, seats):
        print('='*100)
        print('ASIENTOS DISPONIBLES'.center(100))
        print('='*100)
        for i in seats:
            print(str(i[0]) +', ', end = '')
        print('\n' + '='*100)


    def show_tickets(self, tickets):
        print('='*80)
        print(('MIS BOLETOS').center(80))
        print('='*80)
        print('No:'.ljust(5)+'Pelicula:'.ljust(30)+'Fecha:'.ljust(13)+'Hora:'.ljust(12)+'Sala:'.ljust(10)+'Asiento:'.ljust(10))
        print('='*80)
        for r in tickets:
            print(f'{str(r[0]):<5}{r[1]:<30}{str(r[2]):<13}{str(r[3]):<12}{r[4]:<10}{str(r[5]):<10}')
        print('='*80)