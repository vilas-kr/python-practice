-- JOINS
CREATE TABLE Department (
    dept_id INT IDENTITY(1,1),
    dept_name VARCHAR(50),

    CONSTRAINT pk_dept PRIMARY KEY (dept_id)
);

CREATE TABLE Employee (
    emp_id INT IDENTITY(1,1),
    emp_name VARCHAR(50),
    dept_id INT,

    CONSTRAINT pk_emp PRIMARY KEY (emp_id),
    CONSTRAINT fk_emp_dept FOREIGN KEY (dept_id)
        REFERENCES Department(dept_id)
);

INSERT INTO Department (dept_name)
VALUES ('HR'), ('IT'), ('Finance');

INSERT INTO Employee (emp_name, dept_id)
VALUES 
('Vilas', 1),
('Rahul', 2),
('Anita', 2),
('Neha', NULL);

-- Include employees without department
SELECT e.emp_name, d.dept_name
FROM Employee AS e LEFT JOIN Department AS d
ON e.dept_id = d.dept_id;

-- List employees who don’t belong to any department
SELECT e.emp_name
FROM employee AS e LEFT JOIN Department AS d
ON e.dept_id = d.dept_id
WHERE e.dept_id IS NULL;

-- List departments without employees
SELECT d.dept_name
FROM employee AS e RIGHT JOIN Department AS d
ON e.dept_id = d.dept_id
WHERE e.dept_id IS NULL;

-- Count employees per department
SELECT d.dept_name,
       COUNT(e.emp_id) AS employee_count
FROM Department d
LEFT JOIN Employee e
ON d.dept_id = e.dept_id
GROUP BY d.dept_name;

-- Assume tables
/* 
Employee
---------
emp_id (PK)
emp_name
salary
dept_id

Department
---------
dept_id (PK)
dept_name
*/

-- List departments having at least 1 employee
SELECT d.dept_name, COUNT(e.emp_id) AS employee
FROM employee AS e
INNER JOIN Department AS d
ON e.dept_id = d.dept_id
HAVING COUNT(e.emp_id) > 0;

-- Show departments where average salary > overall company average
SELECT d.dept_name, AVG(NULLIF(e.salary, 0)) AS avg_salary
FROM employee AS e 
INNER JOIN Department AS d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING AVG(NULLIF(e.salary, 0)) > ( SELECT AVG(NULLIF(salary, 0))
                                    FROM employee );

-- Count employees per department but show only departments with ≥ 3 employees
SELECT d.dept_id, COUNT(*) AS emp_count
FROM employee AS e
INNER JOIN Department AS d
ON e.dept_id = d.dept_id
GROUP BY d.dept_id
HAVING COUNT(*) > 2

-- Find departments having no employees (JOIN + GROUP BY only)
SELECT d.dept_id, COUNT(e.emp_id) AS emp_count
FROM Department AS d
LEFT JOIN employee AS e
ON d.dept_id = e.dept_id
GROUP BY d.dept_id
HAVING COUNT(e.emp_id) = 0

-- Employees earning more than company average
SELECT e.emp_id
FROM employee AS e
WHERE e.salary > ( SELECT AVG(salary) 
                 FROM employee
                );

-- Employees earning more than their department average (correlated)
SELECT e1.emp_id
FROM employee AS e1
WHERE e1.salary > ( SELECT AVG(e2.salary)
                 FROM employee AS e2
                 WHERE e1.dept_id = e2.dept_id );

-- Departments having no employees (NOT EXISTS)
SELECT d.dept_id
FROM Department as d
WHERE NOT EXISTS ( SELECT 1
                  FROM employee as e
                  WHERE d.dept_id = e.dept_id );

-- Employees who belong to departments located in ‘Mumbai’
SELECT e.emp_id
FROM employee AS e
WHERE e.dept_id IN ( SELECT d.dept_id
                     FROM Department AS d
                     WHERE d.location = 'Mumbai' );

-- Employees whose salary is greater than ALL salaries in HR department
SELECT e.emp_id
FROM employee AS e
WHERE e.salary > ALL ( SELECT e.salary
                       FROM employee AS e
                       INNER JOIN Department AS d
                       ON e.dept_id = d.dept_id
                       WHERE d.dept_name = 'HR' );

