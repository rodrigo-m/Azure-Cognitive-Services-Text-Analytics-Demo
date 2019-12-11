USE [AirBnBSanFrancisco]
GO
CREATE USER [textanalytics] FOR LOGIN [textanalytics] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_datareader] ADD MEMBER [textanalytics]
GO
ALTER ROLE [db_datawriter] ADD MEMBER [textanalytics]
GO
