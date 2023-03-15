-- creates the database hbtn_0d_usa and the table states

-- query that create hbtn_0d_usa if it doen't exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- query that  create table states if doesn't exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
