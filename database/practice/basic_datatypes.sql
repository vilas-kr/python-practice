-- Check version of the SSMS ---
SELECT @@VERSION

-- Shows current database name --
SELECT db_name();

-- List all the databases in the system --
SELECT name
FROM sys.databases;

SELECT DB_NAME() AS CurrentDatabase;

-- Change the database to employee --
USE employee;
GO

SELECT DB_NAME() AS CurrentDatabase;

SELECT name, physical_name
FROM sys.database_files;

CREATE DATABASE practice_db;

USE practice_db;

SELECT DB_NAME();

SELECT name, physical_name
FROM sys.database_files;

-- Creating database with .mdf and .ldf configurations --
CREATE DATABASE TrainingDB2
ON PRIMARY
(
    NAME = TrainingDB2_Data,
    FILENAME = 'D:\Bridgelabs\MSSQL\TrainingDB2.mdf',
    SIZE = 10MB,
    MAXSIZE = 100MB,
    FILEGROWTH = 5MB
)
LOG ON
(
    NAME = TrainingDB2_Log,
    FILENAME = 'D:\Bridgelabs\MSSQL\TrainingDB2.ldf',
    SIZE = 5MB,
    FILEGROWTH = 5MB
);

DROP DATABASE TrainingDB2;

-- Numerical datatypes --
use practice_db;

CREATE TABLE Numeric_Test (
    id int, 
    is_active bit,
    age tinyint,
    score smallint,
    salary decimal(10, 2),
    rating float
);

-- Inserting valid data --
INSERT INTO Numeric_Test 
VALUES (1, 1, 25, 120, 4500.75, 4.5)

-- Inserting Invalid data --
INSERT INTO Numeric_Test 
VALUES (1, 0, 2755, 120, 4500.75, 4.50)

SELECT * FROM Numeric_Test;

-- String Datatypes --
CREATE TABLE String_Test (
    id int,
    code char(5),
    name varchar(50),
    city nvarchar(50),
    description varchar(10)
);

-- Inserting Valid data --
INSERT INTO String_Test
VALUES 
(1, 'A1', 'Vilas', N'Hydrabad', 'Hello');

-- Inserting Invalid data --
INSERT INTO String_Test
VALUES (2, 'B23456', 'Rahul', N'मुंबई', 'This text is too long');

-- Check the length and Bytes taken for city column --
SELECT city, 
       LEN(city) AS len_code,
       DATALENGTH(city) AS bytes_code
FROM String_Test;

SELECT * FROM String_Test;

-- Created a table to test date datatypes
CREATE TABLE Date_Test (
    id int, 
    birth_date date,
    login_time time(3),
    created_dt datetime,
    created_dt2 datetime2(3),
    created_dto datetimeoffset(3)
);

-- Inserting valid data --
INSERT INTO Date_Test VALUES 
(1, '1999-05-10', '10:30:45.123', '2026-01-24 10:30:45.123',
'2026-01-24 10:30:45.123', '2026-01-24 10:30:45.123 +05:30');

-- datetime lower limit test
INSERT INTO Date_Test (id, created_dt)
VALUES (2, '1500-01-01');

SELECT * FROM Date_Test;









