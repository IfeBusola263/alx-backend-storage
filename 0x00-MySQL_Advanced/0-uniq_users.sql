-- Create table for users
-- Schema details will be id, email and name of the user

CREATE TABLE IF NOT EXISTS users (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
email VARCHAR(255) NOT NULL UNIQUE,
name VARCHAR(255));
