-- Create database and new table
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    cities_id INT FOREIGN KEY (id) cities(cities_id),
    name VARCHAR(256) NOT NULL
);