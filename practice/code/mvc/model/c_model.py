from mysql import connector

class Model:
    def __init__(self, config_db_file='c_config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()
        
    def close_db(self):
        self.cnx.close()

    
    """
    # -- CRUD --
    """

    def register(self, u_email, u_password, u_name, admin):
        try :
            sql = 'INSERT INTO users (`u_email`,`u_pass`,`u_name`,`u_admin`) VALUES (%s,%s,%s,%s)'
            vals = (u_email, u_password, u_name, admin)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def login(self, u_email):
        try:
            sql = 'SELECT * FROM users WHERE u_email = %s'
            vals = (u_email,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err



    
    def create_movie(self, m_name, m_duration, m_sday, m_eday):
        try:
            sql = 'INSERT INTO movies (`m_name`, `m_duration`, `m_sday`, `m_eday`) VALUES (%s,%s,%s,%s)'
            vals = (m_name, m_duration, m_sday, m_eday)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_movie(self,id_movie):
        try:
            sql = 'SELECT * FROM movies WHERE id_movie = %s' 
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_movies(self):
        try:
            sql = 'SELECT * FROM movies' 
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_movie(self, fields, vals):
        try:
            sql = 'UPDATE movies SET ' + ','.join(fields)+' WHERE id_movie = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_movie(self, id_movie):
        try:
            sql = 'DELETE FROM movies  WHERE id_movie = %s'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err



    
    #Halls

    def create_hall(self, h_number, h_type, h_price, h_seats):
        try:
            sql = 'INSERT INTO halls (`h_number`,`h_type`, `h_price`, `h_seats`) VALUES (%s,%s,%s,%s)'
            vals = (h_number,h_type, h_price, h_seats)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
        
    def read_halls(self):
        try:
            sql = 'SELECT * FROM halls'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_hall(self, h_number):
        try:
            sql = 'SELECT * FROM halls WHERE h_number = %s'
            vals = (h_number,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def update_hall(self, fields, vals):
        try:
            sql = 'UPDATE halls SET ' + ','.join(fields) + 'WHERE h_number = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_hall(self, id_hall):
        try:
            sql = 'DELETE FROM halls  WHERE h_number = %s'
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    #Seats

    def new_seat(self, s_number, id_sch_data, s_available):
        try:
            sql = 'INSERT INTO seats (`s_number`,`id_sch_data`,`s_available`) VALUES (%s,%s,%s)'
            vals = (s_number, id_sch_data, s_available)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def seats_available(self, id_sch_data):
        try:
            sql = 'SELECT seats.s_number FROM seats WHERE id_sch_data = %s AND s_available = True'
            vals = (id_sch_data,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def seat_available(self, s_number, id_sch_data):
        try:
            sql = 'SELECT s_available FROM seats WHERE s_number = %s AND id_sch_data = %s'
            vals = (s_number, id_sch_data)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def update_seats(self, s_number, id_sch_data, s_available):
        try:
            sql = 'UPDATE seats SET s_available = %s WHERE s_number = %s AND id_sch_data = %s'
            vals = (s_available, s_number, id_sch_data)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_seat(self, id_sch_data):
        try:
            sql = 'DELETE FROM seats  WHERE id_sch_data = %s'
            vals = (id_sch_data,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    


    # Schedule

    def create_schedule(self, sc_time, sc_date):
        try:
            sql = 'INSERT INTO schedules (`sc_time`, `sc_date`) VALUES(%s,%s)'
            vals = (sc_time, sc_date)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_schedules(self):
        try:
            sql = 'SELECT * FROM schedules'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_schedule(self, id_schedule):
        try:
            sql = 'SELECT * FROM schedules WHERE id_schedule = %s'
            vals = (id_schedule,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def update_schedule(self, fields, vals):
        try:
            sql = 'UPDATE schedules SET ' + ','.join(fields) + 'WHERE id_schedule = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_schedule(self, id_schedule):
        try:
            sql = 'DELETE FROM schedules  WHERE id_schedule = %s'
            vals = (id_schedule,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
        


    #Sch_data

    def create_schedule_data(self, id_schedule, id_movie, h_number):
        try:
            sql = 'INSERT INTO schedule_data (`id_schedule`,`id_movie`,`h_number`) VALUES (%s,%s,%s)'
            vals = (id_schedule, id_movie, h_number)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err


    def read_idsch_data(self, id_schedule, h_number):
        try:
            sql = 'SELECT schedule_data.id_sch_data FROM schedule_data WHERE id_schedule = %s AND h_number = %s'
            vals = (id_schedule, h_number)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_sch_data_sch(self, id_sch_data):
        try:
            sql = 'SELECT schedule_data.id_sch_data, movies.m_name, schedules.sc_time, schedules.sc_date, halls.h_number, halls.h_type, halls.h_price FROM schedule_data JOIN (movies, halls, schedules) ON schedule_data.id_movie = movies.id_movie AND schedule_data.id_sch_data = %s AND schedule_data.id_schedule = schedules.id_schedule AND schedule_data.h_number = halls.h_number'
            vals = (id_sch_data,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_sch_data(self, id_movie):
        try:
            sql = 'SELECT schedule_data.id_sch_data, movies.m_name, schedules.sc_time, schedules.sc_date, halls.h_type, halls.h_price FROM schedule_data JOIN (movies, halls, schedules) ON schedule_data.id_movie = movies.id_movie AND schedule_data.id_movie = %s AND schedule_data.id_schedule = schedules.id_schedule AND schedule_data.h_number = halls.h_number'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_sch_data_date(self, date):
        try:
            sql = 'SELECT schedule_data.id_sch_data, movies.m_name, schedules.sc_time, schedules.sc_date, halls.h_type, halls.h_price FROM schedule_data JOIN (movies, halls, schedules) ON schedule_data.id_movie = movies.id_movie AND schedule_data.id_schedule = schedules.id_schedule AND schedules.sc_date = %s AND schedule_data.h_number = halls.h_number'
            vals = (date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_all_sch_data(self):
        try:
            sql = 'SELECT schedule_data.id_sch_data, movies.m_name, schedules.sc_time, schedules.sc_date, halls.h_type, halls.h_price FROM schedule_data JOIN (movies, halls, schedules) ON schedule_data.id_movie = movies.id_movie AND schedule_data.id_schedule = schedules.id_schedule AND schedule_data.h_number = halls.h_number'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_sch_data(self, id_schedule):
        try:
            sql = 'DELETE FROM schedule_data WHERE id_schedule = %s'
            vals = (id_schedule,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err



    #Users

    def read_user(self, id_client):
        try:
            sql = 'SELECT * FROM users WHERE id_client = %s'
            vals = (id_client,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_users(self):
        try:
            sql = 'SELECT * FROM users WHERE u_admin = False'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_admins(self):
        try:
            sql = 'SELECT * FROM users WHERE u_admin = True'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_accounts(self):
        try:
            sql = 'SELECT * FROM users'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def update_privileges(self, id_client, u_admin):
        try:
            sql = 'UPDATE users SET u_admin = %s WHERE id_client = %s'
            vals = (u_admin, id_client)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 


    def buy_ticket(self, id_sch_data, s_number, id_client):
        try:
            sql = 'INSERT INTO tickets (`id_sch_data`,`s_number`, `id_client`) VALUES (%s,%s,%s)'
            vals = (id_sch_data, s_number, id_client)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_tickets(self, id_client):
        try:
            sql = 'SELECT tickets.id_ticket, movies.m_name, schedules.sc_date, schedules.sc_time, schedule_data.h_number, tickets.s_number FROM (schedule_data, tickets) JOIN (movies, schedules) ON tickets.id_sch_data = schedule_data.id_sch_data AND tickets.id_client = %s AND schedule_data.id_schedule = schedules.id_schedule AND schedule_data.id_movie = movies.id_movie'
            vals = (id_client,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            self.cnx.rollback()
            return err