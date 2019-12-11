/* Make sure master is selected */
use master
go

if SUSER_ID ('textanalytics') is not NULL      
    drop login textanalytics
GO

create login [textanalytics] 
    with password = 'Adieohrtrwddko983kd'
go