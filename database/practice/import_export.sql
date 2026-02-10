use lms_db;
go



select * from lms.users;
go

-- Enable ACE in SQL server
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;

EXEC sp_configure 'Ad Hoc Distributed Queries', 1;
RECONFIGURE;

EXEC master.dbo.sp_MSset_oledb_prop
    N'Microsoft.ACE.OLEDB.16.0',
    N'AllowInProcess',
    1;
GO

EXEC master.dbo.sp_MSset_oledb_prop
    N'Microsoft.ACE.OLEDB.16.0',
    N'DynamicParameters',
    1;
GO

-- bcp lms_db.lms.users format nul -c -t, -f D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.fmt -T -S .

SELECT *
FROM OPENROWSET(
    BULK 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv',
    FORMATFILE = 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.fmt'
) AS filedata;

-- linked queries
use demo;
go

CREATE TABLE [users](
	[user_id] [char](9) NOT NULL,
	[name] [varchar](50) NULL,
	[email] [varchar](256) NULL,
	[password] [varchar](50) NULL
	);
go
 
-- Import data form other database
INSERT INTO users
SELECT * 
FROM lms_db.lms.users;
GO

SELECT * FROM users;
GO

-- user defined functions
USE practice;
GO

CREATE TABLE employee (
    emp_id      INT PRIMARY KEY,
    emp_name    VARCHAR(50),
    department  VARCHAR(30),
    designation VARCHAR(30),
    salary      DECIMAL(10,2),
    hire_date   DATE
);
GO

INSERT INTO employee (emp_id, emp_name, department, designation, salary, hire_date)
VALUES
(1, 'Ramesh', 'IT', 'Software Engineer', 55000, '2022-06-15'),
(2, 'Suresh', 'HR', 'HR Executive', 42000, '2021-03-10'),
(3, 'Anita', 'Finance', 'Accountant', 48000, '2020-11-25'),
(4, 'Priya', 'IT', 'Data Analyst', 60000, '2023-01-05'),
(5, 'Kiran', 'Sales', 'Sales Manager', 65000, '2019-08-18');
GO

SELECT * FROM employee;
GO

-- Scaler function
CREATE FUNCTION hikesalary(@salary FLOAT)
RETURNS FLOAT
BEGIN
    RETURN @salary * 1.1
END;
GO

SELECT salary, dbo.hikesalary(salary) AS hikesalary
FROM employee;
GO

-- Table valued function
CREATE FUNCTION GetEmployeeByDepartment(@department VARCHAR(30))
RETURNS TABLE
AS
RETURN
(
    SELECT * 
    FROM employee
    WHERE department = @department
);
GO

SELECT * FROM GetEmployeeByDepartment('IT');
GO

-- Pivot Table

-- Count Employee in IT, HR, SALES department
SELECT *
FROM
(
    SELECT department, emp_id
    FROM employee
) AS src
PIVOT
(
    COUNT(emp_id)
    FOR department IN ([IT], [HR], [Sales]) -- must hard-code column names
) AS p;
GO

-- total salary of IT, HR, SALES department
SELECT *
FROM
(
    SELECT department, salary
    FROM employee
) AS source_table
PIVOT
(
    SUM(salary)
    FOR department IN ([IT], [HR], [Sales])
) AS pivot_table;
GO

--  unpivot table
SELECT department, total_salary
FROM
(
    SELECT [IT], [HR], [Sales]
    FROM salary_pivot
) p
UNPIVOT
(
    total_salary FOR department IN ([IT], [HR], [Sales])
) u;

-- XML path
SELECT emp_name
FROM employee
FOR XML PATH('');
GO

-- Each row → one XML element, Columns become attributes
SELECT emp_id, emp_name, department
FROM employee
FOR XML AUTO;
GO

-- You define element names, Can generate nested XML
SELECT emp_name AS 'Name',
       department AS 'Department'
FROM employee
FOR XML PATH('Employee');
GO




