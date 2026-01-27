USE practice_db;

-- Date functions
SELECT 
  GETDATE() AS getdate,
  CURRENT_TIMESTAMP AS current_ts,
  SYSDATETIME() AS sys_dt,
  SYSDATETIMEOFFSET() AS sys_dto,
  GETUTCDATE() AS utc_dt;

SELECT 
  DATEADD(day, 7, GETDATE()) AS after_7_days,
  DATEDIFF(day, '2026-01-01', GETDATE()) AS days_from_2026;

-- String Functions

-- length of string 
SELECT LEN('SQL   ') AS len_value; 

SELECT DATALENGTH('SQL   ') AS bytes_value;

SELECT SUBSTRING('Microsoft SQL Server', 11, 3);

SELECT LEFT('Database', 4);   -- Data
SELECT RIGHT('Database', 4);  -- base

SELECT CHARINDEX('SQL', 'Microsoft SQL Server');

SELECT PATINDEX('%SQL%', 'Microsoft SQL Server');

SELECT REPLACE('2026-01-24', '-', '/');

SELECT TRIM('   SQL Server   ');
SELECT LTRIM(RTRIM('   SQL   '));

SELECT UPPER('sql server');
SELECT LOWER('SQL SERVER');

SELECT CONCAT('SQL', ' ', 'Server');

SELECT REVERSE('Database');

SELECT STUFF('SQLServer', 4, 6, ' Server');

-- Null functions
SELECT * 
FROM String_Test
WHERE name IS NULL;

SELECT 
    ISNULL(name, 'N/A') AS name
FROM String_Test;

COALESCE(expr1, expr2, expr3)

SELECT NULLIF(10, 10);  -- NULL
SELECT NULLIF(10, 5);   -- 10

CREATE TABLE Null_Test (
    id INT,
    name VARCHAR(50),
    salary INT,
    bonus INT,
    phone VARCHAR(15)
);

INSERT INTO Null_Test VALUES
(1, 'Vilas', 50000, 5000, '9999999999'),
(2, 'Rahul', NULL, 3000, NULL),
(3, 'Anita', 45000, NULL, '8888888888'),
(4, 'Neha', NULL, NULL, NULL);

-- Show salary, but display 0 instead of NULL.
SELECT ISNULL(salary, 0) as salary
FROM Null_Test;

-- Display first available contact (phone → 'Not Provided').
SELECT ISNULL(phone, 'Not Provided') AS phone_number
FROM Null_Test;

-- Calculate total income = salary + bonus, handle NULLs correctly.
SELECT ISNULL(salary, 0) + ISNULL(bonus, 0) AS total_income
FROM Null_Test;

-- Find employees who don’t have salary assigned.
SELECT * 
FROM Null_Test
WHERE salary IS NULL;

-- Avoid divide-by-zero
SELECT salary / NULLIF(bonus, 0) AS bonus_ratio
FROM Null_Test
WHERE salary IS NOT NULL;

-- Total employees
SELECT COUNT(*)
FROM Null_Test;

-- Employees with salary
SELECT *
FROM Null_Test
WHERE salary IS NOT NULL;

-- Employees without salary
SELECT * 
FROM Null_Test
WHERE salary IS NULL;

-- Total salary
SELECT SUM(salary) AS total_salary
FROM Null_Test;

-- Average salary
SELECT AVG(ISNULL(salary, 0)) AS avg_salary
FROM Null_Test;

-- Find total income
SELECT ISNULL(salary, 0) + ISNULL(bonus, 0) AS 'total income'
FROM Null_Test;

-- Find employees whose salary is above average salary
SELECT * 
FROM Null_Test
WHERE salary > (
    SELECT AVG(ISNULL(salary, 0)) AS avg_salary
    FROM Null_Test
    );
                    

-- Group by bonus and count employees
SELECT COUNT(*), bonus
FROM Null_Test
GROUP BY bonus;

-- Count employees per bonus excluding NULL bonuses
SELECT COUNT(*), bonus
FROM Null_Test
WHERE bonus IS NOT NULL
GROUP BY bonus;

-- Show bonus groups having more than 1 employee
SELECT COUNT(*) AS count, bonus
FROM Null_Test
WHERE bonus IS NOT NULL
GROUP BY bonus
HAVING COUNT(*) > 1;

-- Find average salary per bonus
SELECT AVG(salary) AS avg_salary, bonus
FROM Null_Test
GROUP BY bonus;

-- Find bonus groups where average salary > 45000
SELECT AVG(salary) AS avg_salary, bonus
FROM Null_Test
GROUP BY bonus
HAVING AVG(salary) > 45000;

-- Group employees into: Has Salary, No Salary and count them
SELECT 
    CASE 
        WHEN salary IS NOT NULL THEN 'Has Salary'
        ELSE 'No Salary'
    END AS Salary_Group,
    COUNT(*) AS count
FROM Null_Test
GROUP BY 
    CASE 
        WHEN salary IS NOT NULL THEN 'Has Salary'
        ELSE 'No Salary'
    END;


-- Constraints

/* Create a table Users with:
user_id → PK + identity
email → UNIQUE + NOT NULL
age → must be ≥ 18
created_at → default current date */

CREATE TABLE users (
user_id INT,
email VARCHAR(50),
age TINYINT,
create_at DATETIME2 DEFAULT GETDATE(),
CONSTRAINT uq_email UNIQUE(email),
CONSTRAINT pk PRIMARY KEY(user_id),
CONSTRAINT ck_age CHECK(age >= 18)
);

-- One valid row
INSERT INTO users (user_id, email, age) VALUES
    (1, 'vilas@gmail.com', 21);

-- One invalid row (age < 18)
INSERT INTO users (user_id, email, age) VALUES
    (2, 'vinay@gmail.com', 17);

-- One duplicate email
INSERT INTO users (user_id, email, age) VALUES
    (3, 'vilas@gmail.com', 31);

-- Try inserting NULL into UNIQUE column
INSERT INTO users (user_id, age) VALUES
    (3, 31);

SELECT * FROM users;

/* Create a table with:
salary must be > 0
salary cannot be NULL */
CREATE TABLE employee (
    id INT,
    name VARCHAR(50),
    salary DECIMAL(10,2) NOT NULL,
    CONSTRAINT ck_salary CHECK(salary > 0)
);

