from model.c_model import Model
from view.c_view import View
from datetime import datetime

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.start_menu()

    def start_menu(self):
        o='0'
        while o != 4:
            self.view.header('MENU')
            self.view.start_menu()
            self.view.opcion('3')
            o = input()

            if o == '1':
                self.login()
            elif o == '2':
                self.reg_menu()
            elif o == '3':
                return
            else:
                self.view.not_valid_op()

    def update_lists(self,fs,vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals
            
    def reg_menu(self):
        o='0'
        while o != 3:
            self.view.header('REGISTRO')
            self.view.reg_menu()
            self.view.opcion('3')
            o = input()

            if o == '1':
                self.u_register()
            elif o == '2':
                self.a_register()
            elif o == '3':
                return
            else:
                self.view.not_valid_op()

        
    def ask_login(self):
        print('Correo: ', end = '')
        u_email = input()
        print('Contraseña: ', end = '')
        u_pass = input()
        return [u_email, u_pass]

    def ask_register(self):
        print('Correo: ', end = '')
        u_email = input()
        print('Contraseña: ', end = '')
        u_pass = input()
        print('Nombre: ', end = '')
        u_name = input()
        return [u_email, u_pass, u_name]

    def ask_movie(self):
        print('Titulo: ', end = '')
        m_name = input()
        print('Duracion (hh:mm:ss): ', end = '')
        m_duration = input()
        print('Dia inicio (YYYY-MM-DD): ', end = '')
        m_sday = input()
        print('Dia final (YYYY-MM-DD): ', end = '')
        m_eday = input()
        return [m_name, m_duration, m_sday, m_eday]

    def ask_hall(self):
        print('Tipo de sala: ', end = '')
        h_type = input()
        print('Precio: $', end = '')
        h_price = input()
        return [h_type, h_price]

    def ask_schedule(self):
        print('Hora de funcion (hh:mm:ss): ', end = '')
        sc_time = input()
        print('Fecha de funcion (YYYY-MM-DD): ', end = '')
        sc_date = input()
        return [sc_time, sc_date]

    def ask_m_schedule(self):
        print('Id Horario: ', end = '')
        id_schedule = input()
        print('Id Pelicula: ', end = '')
        id_movie = input()
        print('Id Sala: ', end = '')
        h_number = input()
        return [id_schedule, id_movie, h_number]



    def login(self):
        self.view.header('LOGIN')
        u_email, u_pass = self.ask_login()
        user = self.model.login(u_email)
        if user == None:
            self.view.error('USUARIO NO REGISTRADO')
        elif u_pass == user[2]:
            self.view.valid_op('CONECTADO')
            if user[4] == True:
                self.a_menu(user)
            elif user[4] == False:
                self.u_menu(user)
        else:
            self.view.error('CONTRASEÑA INCORRECTA')

    def u_register(self):
        self.view.header('REGISTRO USUARIO')
        u_email, u_pass, u_name = self.ask_register()
        reg = self.model.register(u_email, u_pass, u_name, False)
        if reg == True:
            self.view.valid_op('USUARIO REGISTRADO')
        else:
            self.view.error('NO FUE POSIBLE REGISTRAR')

    def a_register(self):
        self.view.header('REGISTRO ADMIN')
        a_email, a_pass, a_name = self.ask_register()
        reg = self.model.register(a_email, a_pass, a_name, True)
        if reg == True:
            self.view.valid_op('ADMIN REGISTRADO')
        else:
            self.view.error('NO FUE POSIBLE REGISTRAR')



    def u_menu(self, user):
        o = '0'
        while o != 6:
            self.view.header('MENU USUARIO')
            self.view.u_menu(user[3])
            self.view.opcion('6')
            o = input()
            if o == '1':
                self.buy_ticket(user[0])
            elif o == '2':
                self.show_tickets(user[0])
            elif o == '3':
                self.show_all_sch_data()
            elif o == '4':
                self.show_sch_data()
            elif o == '5':
                self.show_sch_data_date()
            elif o == '6':
                return
            else:
                self.view.not_valid_op()

    def a_menu(self, user):
        o = '0'
        while o != 6:
            self.view.header('MENU ADMIN')
            self.view.a_menu(user[3])
            self.view.opcion('6')
            o = input()
            if o == '1':
                self.halls_menu()
            elif o == '2':
                self.seats_menu()
            elif o == '3':
                self.movies_menu()
            elif o == '4':
                self.schedule_menu()
            elif o == '5':
                self.admins_menu()
            elif o == '6':
                return
            else:
                self.view.not_valid_op()


    #Movies

    def movies_menu(self):
        o = '0'
        while o != 6:
            self.view.header('MENU PELICULAS')
            self.view.movies_menu()
            self.view.opcion('6')
            o = input()
            if o == '1':
                self.add_movie()
            elif o == '2':
                self.show_movies()
            elif o == '3':
                self.show_movie()
            elif o == '4':
                self.update_movie()
            elif o == '5':
                self.delete_movie()
            elif o == '6':
                return
            else:
                self.view.not_valid_op()


    def add_movie(self):
        self.view.header('NUEVA PELICULA')
        m_name, m_duration, m_sday, m_eday = self.ask_movie()
        out = self.model.create_movie(m_name, m_duration, m_sday, m_eday)
        if out == True:
            self.view.valid_op('PELICULA CREADA')
        else:
            self.view.error('PELICULA NO AGREGADA')

    def show_movies(self):
        movies = self.model.read_movies()
        if type(movies) == list:
            self.view.show_movies(movies)
        else:
            self.view.error('PROBLEMA AL VER PELICULAS')
        return

    def show_movie(self):
        self.view.header('VER PELICULA')
        self.view.ask('Id Pelicula: ')
        id_movie = input()
        movie = self.model.read_movie(id_movie)
        if type(movie) == tuple:
            self.view.show_movie(movie)
        else:
            self.view.error('PROBLEMA AL VER PELICULA')
        return

    def update_movie(self):
        self.view.header('EDITAR PELICULA')
        self.view.ask('Id Pelicula: ')
        id_movie = input()
        movie = self.model.read_movie(id_movie)
        if type(movie) == tuple:
            self.view.show_movie(movie)    
        else:
            if movie == None:
                self.view.error('PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')

        all_vals = self.ask_movie()
        fields, vals = self.update_lists(['m_name','m_duration','m_sday','m_eday'],all_vals)
        vals.append(id_movie)
        movie = self.model.update_movie(fields, vals)
        if movie == True:
            self.view.valid_op('PELICULA EDITADA')
        else:
            self.view.error('PELICULA NO EDITADA')

    def delete_movie(self):
        self.view.header('BORRAR PELICULA')
        self.view.ask('Id Pelicula: ')
        id_movie = input()
        count = self.model.delete_movie(id_movie)
        if count != 0:
            self.view.valid_op('SE BORRO LA PELICULA')
        else:
            if count == 0:
                self.view.error('PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR PELICULA')
        return



    #Asientos

    def seats_menu(self):
        o = '0'
        while o != 3:
            self.view.header('MENU ASIENTOS')
            self.view.seats_menu()
            self.view.opcion('3')
            o = input()
            if o == '1':
                self.seats_show_a(True)
            elif o == '2':
                self.seats_show_a(False)
            elif o == '3':
                return
            else:
                self.view.not_valid_op()

    def seats_show_a(self, available):
        sch_data = self.model.read_all_sch_data()
        if type(sch_data) == list:
            self.view.show_sch_data(sch_data)
            print('Id Funcion: ', end = '')
            id_sch_data = input()
            seats = self.model.seats_available(id_sch_data, available)
            if type(seats) == list:
                self.view.seats_available(seats)
            else:
                self.view.error('PROBLEMA AL VER ASIENTOS')
            return
        else:
            self.view.error('PROBLEMA AL VER HORARIOS DE PELICULAS')
    
    #Salas

    def halls_menu(self):
        o = '0'
        while o != 5:
            self.view.header('MENU SALAS')
            self.view.halls_menu()
            self.view.opcion('5')
            o = input()
            if o == '1':
                self.add_hall()
            elif o == '2':
                self.show_halls()
            elif o == '3':
                self.update_hall()
            elif o == '4':
                self.delete_hall()
            elif o == '5':
                return
            else:
                self.view.not_valid_op()

    def add_hall(self):
        self.view.header('NUEVA SALA')
        print('Numero de sala: ', end = '')
        h_number = input()
        h_type, h_price = self.ask_hall()
        print('No. de asientos: ', end = '')
        h_seats = input()
        out = self.model.create_hall(h_number, h_type, h_price, h_seats)
        if out == True:
            self.view.valid_op('SALA CREADA')
        else:
            self.view.error('SALA NO AGREGADA')

    def show_halls(self):
        halls = self.model.read_halls()
        if type(halls) == list:
            self.view.show_halls(halls)
        else:
            self.view.error('PROBLEMA AL VER SALAS')
        return

    def update_hall(self):
        self.view.header('EDITAR SALA')
        self.view.ask('Id Sala: ')
        h_number = input()
        hall = self.model.read_hall(h_number)
        if type(hall) == tuple:
            self.view.show_hall(hall)    
        else:
            if hall == None:
                self.view.error('SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER SALA') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')

        all_vals = self.ask_hall()
        fields, vals = self.update_lists(['h_type','h_price'],all_vals)
        vals.append(h_number)
        hall = self.model.update_hall(fields, vals)
        if hall == True:
            self.view.valid_op('SALA EDITADA')
        else:
            self.view.error('SALA NO EDITADA')

    def delete_hall(self):
        self.view.header('BORRAR SALA')
        self.view.ask('Id Sala: ')
        h_number = input()
        count = self.model.delete_hall(h_number)
        if count != 0:
            self.view.valid_op('SE BORRO LA SALA')
        else:
            if count == 0:
                self.view.error('SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA SALA')
        return



    #schedule

    def schedule_menu(self):
        o = '0'
        while o != 6:
            self.view.header('MENU HORARIOS')
            self.view.schedule_menu()
            self.view.opcion('6')
            o = input()
            if o == '1':
                self.create_schedule()
            elif o == '2':
                self.create_m_schedule()
            elif o == '3':
                self.show_schedules()
            elif o == '4':
                self.show_all_sch_data()
            elif o == '5':
                self.show_sch_data()
            elif o == '6':
                self.update_schedule()
            elif o == '7':
                self.delete_schedule()
            elif o == '8':
                return
            else:
                self.view.not_valid_op()

            
    def create_schedule(self):
        self.view.header('NUEVO HORARIO')
        sc_time, sc_date = self.ask_schedule()
        out = self.model.create_schedule(sc_time, sc_date)
        if out == True:
            self.view.valid_op('HORARIO CREADO')
        else:
            self.view.error('HORARIO NO AGREGADO')

    def create_m_schedule(self):
        self.show_schedules()
        self.show_movies()
        self.show_halls()
        self.view.header('HORARIO PELICULA')
        id_schedule, id_movie, h_number = self.ask_m_schedule()
        out = self.model.create_schedule_data(id_schedule, id_movie, h_number)
        seats = self.model.read_hall(h_number)
        id_sch_data = self.model.read_idsch_data(id_schedule, h_number)
        if out == True:
            self.view.valid_op('HORARIO DE PELICULA CREADO')
            for s in range(1, seats[3]+1):
                out2 = self.model.new_seat(s, id_sch_data[0], True)
            if out2 == True:
                self.view.valid_op('ASIENTOS CREADOS')
            else:
                self.view.error('ASIENTOS NO AGREGADOS')
        else:
            self.view.error('HORARIO DE PELICULA NO AGREGADO')


    def show_schedules(self):
        schedules = self.model.read_schedules()
        if type(schedules) == list:
            self.view.show_schedules(schedules)
        else:
            self.view.error('PROBLEMA AL VER HORARIOS')
        return

    def update_schedule(self):
        self.view.header('EDITAR HORARIO')
        self.view.ask('Id Horario: ')
        id_schedule = input()
        schedule = self.model.read_schedule(id_schedule)
        if type(schedule) == tuple:
            self.view.show_schedule(schedule)    
        else:
            if schedule == None:
                self.view.error('HORARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER HORARIO') 
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        all_vals = self.ask_schedule()
        fields, vals = self.update_lists(['sc_time','sc_date'],all_vals)
        vals.append(id_schedule)
        schedule = self.model.update_schedule(fields, vals)
        if schedule == True:
            self.view.valid_op('HORARIO EDITADO')
        else:
            self.view.error('HORARIO NO EDITADO')

    def delete_schedule(self):
        self.view.header('BORRAR HORARIO')
        self.view.ask('Id Horario: ')
        id_schedule = input()
        count = self.model.delete_schedule(id_schedule)
        if count != 0:
            self.view.valid_op('SE BORRO EL HORARIO')
        else:
            if count == 0:
                self.view.error('HORARIO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR HORARIO')
        return



    def show_sch_data(self):
        self.show_movies()
        print('Id Pelicula: ', end = '')
        id_movie = input()
        sch_data = self.model.read_sch_data(id_movie)
        if type(sch_data) == list:
            self.view.show_sch_data(sch_data)
        else:
            self.view.error('PROBLEMA AL VER HORARIOS DE PELICULAS')
        return

    def show_sch_data_date(self):
        print('Fecha (YYYY-MM-DD): ', end = '')
        date = input()
        sch_data = self.model.read_sch_data_date(date)
        if type(sch_data) == list:
            self.view.show_sch_data(sch_data)
        else:
            self.view.error('PROBLEMA AL VER HORARIOS DE PELICULAS')
        return

    def show_all_sch_data(self):
        sch_data = self.model.read_all_sch_data()
        if type(sch_data) == list:
            self.view.show_sch_data(sch_data)
        else:
            self.view.error('PROBLEMA AL VER HORARIOS DE PELICULAS')
        return



    
    def admins_menu(self):
        o = '0'
        while o != 5:
            self.view.header('MENU ADMINISTRADORES')
            self.view.admins_menu()
            self.view.opcion('5')
            o = input()
            if o == '1':
                self.show_users()
            elif o == '2':
                self.show_admins()
            elif o == '3':
                self.show_accounts()
            elif o == '4':
                self.acc_privileges()
            elif o == '5':
                return
            else:
                self.view.not_valid_op()

    def show_users(self):
        users = self.model.read_users()
        if type(users) == list:
            self.view.show_users(users, 'NORMALES')
        else:
            self.view.error('PROBLEMA AL LEER CUENTAS')
        return

    def show_admins(self):
        admins = self.model.read_admins()
        if type(admins) == list:
            self.view.show_users(admins, 'ADMINISTRADORES')
        else:
            self.view.error('PROBLEMA AL LEER CUENTAS')
        return

    def show_accounts(self):
        accs = self.model.read_accounts()
        if type(accs) == list:
            self.view.show_accs(accs)
        else:
            self.view.error('PROBLEMA AL LEER CUENTAS')
        return

    def acc_privileges(self):
        self.view.header('PRIVILEGIOS DE CUENTA')
        print('Id cuenta: ', end = '')
        id_client = input()
        user = self.model.read_user(id_client)
        self.view.show_acc(user)
        if user[4] == False:
            print('¿Desea dar privilegios de administrador a este usuario? (y/n): ', end = '')
            confirm = input()
            if confirm == 'y':
                confirm = self.model.update_privileges(id_client, True)
                if confirm == True:
                    self.view.valid_op('NUEVO ADMINISTRADOR')
                else:
                    self.view.error('NO SE PUDO CAMBIAR PRIVILEGIOS')

            else:
                self.view.msg('CAMBIO NO REALIZADO')
        elif user[4] == True:
            print('¿Desea revocar privilegios de administrador a este usuario? (y/n): ', end = '')
            confirm = input()
            if confirm == 'y':
                confirm = self.model.update_privileges(id_client, False)
                if confirm == True:
                    self.view.valid_op('ADMINISTRADOR ELIMINADO')
                else:
                    self.view.error('NO SE PUDO CAMBIAR PRIVILEGIOS')

            else:
                self.view.msg('CAMBIO NO REALIZADO')
        else:
            self.view.error('NO SE PUDO REALIZAR LA OPERACION')


    def buy_ticket(self, id_client):
        sch_data = self.model.read_all_sch_data()
        if type(sch_data) == list:
            self.view.show_sch_data(sch_data)
        else:
            self.view.error('PROBLEMA AL VER HORARIOS DE PELICULAS')
        print('No de horario: ', end = '')
        id_sch_data = input()
        seats = self.model.seats_available(id_sch_data, True)
        self.view.seats_available(seats)
        print('Asiento: ', end = '')
        s_number = input()
        s_a = self.model.seat_available(s_number, id_sch_data)
        if s_a[0] == True:
            out = self.model.buy_ticket(id_sch_data, s_number, id_client)
            if out == True:
                self.view.valid_op('BOLETO COMPRADO')
                self.model.update_seats(s_number,id_sch_data,False)
            else:
                self.view.error('FALLO AL COMPRAR BOLETO')
        else:
            self.view.error('ASIENTO NO DISPONIBLE')

    def show_tickets(self, id_client):
        tickets = self.model.read_tickets(id_client)
        if type(tickets) == list:
            self.view.show_tickets(tickets)
        else:
            self.view.error('PROBLEMA AL LEER TICKETS')
        return