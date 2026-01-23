USE Employee_db;

SELECT * FROM Employee;

SELECT * FROM SYS.TABLES;

--DDL
ALTER TABLE Employee
ADD  emp_salary INT not null;

INSERT INTO Employee VALUES(101,'SUDHEER','SUDHEER@GMAIL.COM',50000);

CREATE TABLE DEPT 
(dept_id int primary key,
dept_name varchar(20) not null)

SELECT * FROM DEPT;

INSERT INTO DEPT VALUES(201,'IT');

EXEC SP_RENAME 'DBO.Employee','EMPLOYEE';

CREATE TABLE SAMPLE(
ID INT  not null ,
NAME VARCHAR(20) not null );

TRUNCATE TABLE SAMPLE;

DROP TABLE SAMPLE;

SELECT * FROM SYS.TABLES;

TRUNCATE TABLE DEPT;

TRUNCATE TABLE EMPLOYEE;

ALTER TABLE EMPLOYEE
DROP COLUMN emp_email;

--DML
INSERT INTO DEPT VALUES 
(10, 'HR'),
(20, 'IT'),
(30, 'Finance'),
(40, 'Sales');

ALTER TABLE EMPLOYEE
ADD dept_id INT;

INSERT INTO EMPLOYEE VALUES
(1, 'Rahul', 50000, 10),
(2, 'Anita', 65000, 20),
(3, 'Kiran', 55000, 20),
(4, 'Neha', 60000, 30);

ALTER TABLE EMPLOYEE 
ADD CONSTRAINT FK_DEPTID
FOREIGN KEY (dept_id)
REFERENCES DEPT(dept_id);

SELECT E.emp_name, D.dept_name
FROM EMPLOYEE E LEFT JOIN DEPT D
ON E.dept_id = D.dept_id;
--WHERE D.dept_id = 10;

SELECT * FROM DEPT;

UPDATE DEPT
SET dept_id = 50
WHERE dept_name = 'Sales';

INSERT INTO DEPT VALUES(1,'RR');

DELETE 
FROM DEPT 
WHERE dept_id = 1;

--DQL
select * from EMPLOYEE;

--TCL
BEGIN TRANSACTION
INSERT INTO DEPT VALUES (90,'ACCOUNTS');

SAVE Transaction T1;

delete 
from DEPT
where dept_id in (80,90);

rollback Transaction T1;

SELECT * FROM DEPT;

--functions
--concat, trim, replace(value,old_char,New_char),lower , upper, right(value,no of letters) , left(value,no of letters),substr(value,start,no of letters))
select substring(emp_name,2,len(emp_name))
from EMPLOYEE

 --CASE 
 SELECT emp_salary ,
CASE
WHEN emp_salary>50000 THEN 'HIGH'
WHEN emp_salary = 50000 THEN 'OK'
ELSE 'WASTE'
END
FROM EMPLOYEE