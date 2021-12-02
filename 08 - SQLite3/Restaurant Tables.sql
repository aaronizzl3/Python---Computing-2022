/* Tables */
CREATE TABLE tblEmployees(
  ID int auto_increment,
  Forename varchar(30) NOT NULL,
  Surname varchar(30) NOT NULL,
  Role varchar(40) DEFAULT 'Waiter',
  PRIMARY KEY (ID)
  );
  
 CREATE TABLE tblShifts(
   ID int auto_increment,
   EmployeeID int,
   ShiftDate date,
   StartTime varchar(30) NOT NULL,
   EndTime varchar(30) NOT NULL,
   PRIMARY KEY (ID)
   );

/* Add Foreign Keys */
ALTER TABLE tblShifts
ADD FOREIGN KEY (EmployeeID)
REFERENCES tblEmployees(ID);