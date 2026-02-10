SELECT *
FROM OPENROWSET(
    BULK 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv',
    FORMAT = 'CSV',
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '\n',
    FIRSTROW = 2
) AS filedata;


SELECT *
FROM OPENROWSET(
    BULK 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv',
    FORMATFILE = 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.fmt'
) AS filedata;

-- Check length of first row password
SELECT LEN(password)
FROM OPENROWSET(
    BULK 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv',
    FORMATFILE = 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.fmt'
) AS filedata;

-- Create a staging table with safe column lengths
CREATE TABLE [users_staging](
    user_id CHAR(9),
    name VARCHAR(50),
    email VARCHAR(256),
    password VARCHAR(255)  -- BIG ENOUGH
);
GO

sp_configure 'show advanced options', 1;
GO
RECONFIGURE;
GO
sp_configure 'Ad Hoc Distributed Queries', 1;
GO
RECONFIGURE;
GO

SELECT *
FROM OPENROWSET(
    BULK 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv',
    FORMATFILE = 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.fmt'
) AS filedata(
    user_id CHAR(9),
    name VARCHAR(50),
    email VARCHAR(256),
    password VARCHAR(255)
);

-- Bulk insert into staging
BULK INSERT [users_staging]
FROM 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv'
WITH (FORMATFILE = 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.fmt', FIRSTROW = 2);
GO

SELECT
    CAST(user_id AS CHAR(9)) AS user_id,
    CAST(name AS VARCHAR(50)) AS name,
    CAST(email AS VARCHAR(256)) AS email,
    CAST(password AS VARCHAR(255)) AS password
FROM OPENROWSET(
    BULK 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv',
    FORMATFILE='D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.fmt'
) AS filedata;


SELECT * 
FROM OPENROWSET(BULK 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv', FORMATFILE='D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.fmt') AS filedata;


EXEC xp_fileexist 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv';

SELECT *
FROM OPENROWSET(
    BULK 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv',
    FORMATFILE = 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.fmt'
) AS filedata(user_id CHAR(9), name VARCHAR(50), email VARCHAR(256), password VARCHAR(255));



use lms_db;
go

ALTER TABLE [lms].[users]
ALTER COLUMN [password] VARCHAR(255) NULL;

ALTER TABLE [lms].[users]
ALTER COLUMN [password] VARCHAR(255) NULL;

select * from lms.users;

use practice1;
go

BULK INSERT [users]
FROM 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv'
WITH (
    FORMATFILE = 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.fmt',
    FIRSTROW = 2
);

select * from users;

create database practice1;
go

CREATE TABLE [users](
	[user_id] [char](9) NOT NULL,
	[name] [varchar](50) NULL,
	[email] [varchar](256) NULL,
	[password] [varchar](255) NULL
);
go

BULK INSERT users
FROM 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\users.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    ROWTERMINATOR = '0x0a',
    TABLOCK
);
GO
