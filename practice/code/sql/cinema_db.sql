CREATE DATABASE IF NOT EXISTS cinema_db;
USE cinema_db;

CREATE TABLE IF NOT EXISTS movies
(
	id_movie INT NOT NULL AUTO_INCREMENT,
    m_name VARCHAR(30) NOT NULL,
    m_duration TIME,
    m_sday DATE,
    m_eday DATE,
    
    PRIMARY KEY (id_movie)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS halls
(
	h_number INT NOT NULL,
    h_type VARCHAR(15) NOT NULL,
    h_price FLOAT NOT NULL,
    h_seats INT NOT NULL,
    
    PRIMARY KEY (h_number)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS schedules
(
	id_schedule INT NOT NULL AUTO_INCREMENT,
    sc_time TIME NOT NULL,
    sc_date DATE NOT NULL,
    
    PRIMARY KEY (id_schedule)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS schedule_data
(
	id_sch_data INT NOT NULL AUTO_INCREMENT UNIQUE,
	id_schedule INT NOT NULL,
    id_movie INT NOT NULL,
    h_number INT NOT NULL,
    
    PRIMARY KEY (id_schedule, h_number),
    CONSTRAINT fk_schedule FOREIGN KEY (id_schedule)
    REFERENCES schedules(id_schedule)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_movie FOREIGN KEY (id_movie)
    REFERENCES movies(id_movie)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_hall FOREIGN KEY (h_number)
    REFERENCES halls(h_number)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS seats
(
	s_number INT NOT NULL,
    id_sch_data INT NOT NULL,
    s_available BOOL NOT NULL,
    
    PRIMARY KEY (s_number, id_sch_data),
    CONSTRAINT fk_sch_data2 FOREIGN KEY (id_sch_data)
    REFERENCES schedule_data(id_sch_data)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS tickets
(
	id_ticket INT NOT NULL AUTO_INCREMENT,
	id_sch_data INT NOT NULL,
    s_number INT NOT NULL,
    id_client INT NOT NULL,
    
    PRIMARY KEY (id_ticket),
    CONSTRAINT fk_sch_data FOREIGN KEY (id_sch_data)
    REFERENCES schedule_data(id_sch_data)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_seat FOREIGN KEY (s_number)
    REFERENCES seats(s_number)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT fk_client FOREIGN KEY (id_client)
    REFERENCES users(id_client)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS users
(
	id_client INT NOT NULL AUTO_INCREMENT,
    u_email VARCHAR(50) NOT NULL UNIQUE,
    u_pass VARCHAR(20) NOT NULL,
    u_name VARCHAR(25) NOT NULL,
    u_admin BOOL,
    
    PRIMARY KEY (id_client)
)ENGINE = INNODB;