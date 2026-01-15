DROP DATABASE IF EXISTS hbtn_0e_0_usa;
CREATE DATABASE hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
