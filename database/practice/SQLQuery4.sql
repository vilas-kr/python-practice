create database practice2;
go

use practice2;
go

create table users(
	name varchar(100),
	salary int,
	id varchar(100)
);
go

SELECT *
FROM OPENROWSET(
    BULK 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\demo1.csv',
    FORMATFILE = 'D:\Bridgelabs\Practice-Problem\database\lms_db\dataset\demo1.fmt',
	FIRSTROW = 2
) AS filedata;


SELECT servicename, service_account
FROM sys.dm_server_services;

select @@VERSION;

RESTORE FILELISTONLY FROM DISK = N'C:\Program Files\Microsoft SQL Server\170\Tools\Binn\SSISDBTemplate.bak'

USE master;
GO
EXEC [catalog].[create_catalog]
     @password = N'vilas';
GO


SELECT name
FROM sys.schemas
WHERE name = 'catalog';


BACKUP DATABASE model 
TO DISK = N'C:\Temp\SSISDBBackup.bak'
WITH INIT, FORMAT;
GO


