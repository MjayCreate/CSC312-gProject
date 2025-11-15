-- create db
CREATE DATABASE flask_app_db;

-- context
USE flask_app_db;

-- create table
CREATE TABLE tbl_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

