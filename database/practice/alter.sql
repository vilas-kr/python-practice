-- Created a new practice database
CREATE DATABASE practice_db;
GO

use practice_db;
GO

-- Change the data types of the columns in the practice.users table to VARCHAR(255)
ALTER TABLE practice.users
ALTER COLUMN name VARCHAR(255);
GO

ALTER TABLE practice.users
ALTER COLUMN email VARCHAR(255);
GO

ALTER TABLE practice.users
ALTER COLUMN password VARCHAR(255);
GO

-- Rename the name column to full_name in the practice.users table
EXEC sp_rename 'practice.users.name', 'full_name', 'COLUMN';
GO

-- Rename the practice.users table to practice.users_info
EXEC sp_rename 'practice.users', 'users_info', 'OBJECT';
GO

SELECT * FROM practice.users_info;
GO


