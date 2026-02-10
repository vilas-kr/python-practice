-- 1. Enable advanced options
EXEC sp_configure 'show advanced options', 1;
GO
RECONFIGURE;
GO

-- 2. Enable CLR
EXEC sp_configure 'clr enabled', 1;
GO
RECONFIGURE;
GO

-- 3. Verify CLR is enabled
EXEC sp_configure 'clr enabled';
GO

USE master;
GO

-- 1. Enable CLR Integration
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'clr enabled', 1;
RECONFIGURE;
GO

-- 2. Create Master Key & Certificate
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'vilas';  -- CHANGE THIS
GO

CREATE CERTIFICATE SSISDBCertificate
WITH SUBJECT = 'SSISDB Certificate', EXPIRY_DATE = '2030-12-31';
GO

-- 3. Backup Certificate
BACKUP CERTIFICATE SSISDBCertificate
TO FILE = 'C:\Temp\SSISDBCertificate.cer'
WITH PRIVATE KEY (
    FILE = 'C:\Temp\SSISDBCertificate.pvk',
    ENCRYPTION BY PASSWORD = 'vilas'  -- SAME PASSWORD
);
GO

-- 4. Create SSISDB Database
CREATE DATABASE SSISDB;
GO

-- 5. Run SSISDB Setup Script (this creates all objects)
DECLARE @sql NVARCHAR(500) = N'
EXEC [SSISDB].[catalog].[configure_catalog];
';
EXEC sp_executesql @sql;
GO

-- 6. Enable SSIS startup procedure
EXEC sp_ssis_startup;
EXEC sp_procoption N'sp_ssis_startup', 'startup', 'on';
GO

-- Check if SSISDB exists and catalog is ready
SELECT name FROM sys.databases WHERE name = 'SSISDB';
SELECT * FROM sys.dm_exec_requests WHERE command LIKE '%SSIS%';


EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'clr enabled', 1;
RECONFIGURE;
GO

-- Master Key & Certificate
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'vilas';  -- Your password
GO

CREATE CERTIFICATE SSISDBCertificate 
WITH SUBJECT = 'SSISDB Certificate', EXPIRY_DATE = '2030-12-31';
GO

-- This creates SSISDB from your backup file
RESTORE FILELISTONLY FROM DISK = 'C:\Program Files\Microsoft SQL Server\170\DTS\Binn\SSISDBBackup.bak';
GO

-- Create SSISDB database from backup
RESTORE DATABASE SSISDB 
FROM DISK = 'C:\Program Files\Microsoft SQL Server\170\DTS\Binn\SSISDBBackup.bak'
WITH MOVE 'SSISDB' TO 'C:\Program Files\Microsoft SQL Server\MSSQL17.MSSQLSERVER\MSSQL\DATA\SSISDB.mdf',
MOVE 'SSISDB_Log' TO 'C:\Program Files\Microsoft SQL Server\MSSQL17.MSSQLSERVER\MSSQL\DATA\SSISDB_Log.ldf',
MOVE 'SSISDB_tempdb' TO 'C:\Program Files\Microsoft SQL Server\MSSQL17.MSSQLSERVER\MSSQL\DATA\SSISDB_tempdb.mdf',
REPLACE;
GO

-- =============================================
-- CREATE SSIS CATALOG - NO BACKUP FILE REQUIRED
-- =============================================
USE master;
GO

-- 1. Prerequisites (already done)
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'clr enabled', 1;
RECONFIGURE;
GO

-- 2. Drop SSISDB if exists (cleanup)
IF EXISTS (SELECT name FROM sys.databases WHERE name = 'SSISDB')
    DROP DATABASE SSISDB;
GO

-- 3. Create security objects
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'vilas';
CREATE CERTIFICATE SSISDBCertificate 
WITH SUBJECT = 'SSISDB Certificate', EXPIRY_DATE = '2030-12-31';
GO

-- 4. Create empty SSISDB database
CREATE DATABASE SSISDB 
COLLATE Latin1_General_CI_AS;
GO

-- 5. Wait for database to be ready
WAITFOR DELAY '00:00:05';
GO

-- 6. Install SSISDB schema from system tables
USE SSISDB;
GO

-- Create basic catalog schema manually
CREATE SCHEMA catalog AUTHORIZATION dbo;
GO

-- Create catalog configuration procedure stub
EXEC ('CREATE PROCEDURE catalog.configure_catalog @password nvarchar(128)
AS BEGIN PRINT ''Catalog configured manually'' END');
GO

EXEC catalog.configure_catalog 'vilas';
GO

USE master;
GO