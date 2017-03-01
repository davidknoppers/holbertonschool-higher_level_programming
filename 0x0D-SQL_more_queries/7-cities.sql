-- creates hbtn_0d_usa database and cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
       id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
       state_id INT, FOREIGN KEY (state_id) REFERENCES states(id) NOT NULL:
       name VARCHAR (256) NOT NULL;
);