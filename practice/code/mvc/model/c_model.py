from mysql import connector

class Model:
    def __init__(self, config_db_file='m_config.txt'):
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