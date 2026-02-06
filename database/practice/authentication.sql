CREATE LOGIN testuser
WITH PASSWORD = 'Test@123';
GO

USE lms_db;
GO

ALTER ROLE db_owner ADD MEMBER testuser;
GO