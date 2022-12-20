"""1"""
SELECT * FROM pds.employees order by LAST_NAME;

"""2"""
SELECT FIRST_NAME, LAST_NAME,  SALARY, (SALARY * 0.15) AS TAX
FROM pds.employees
order by LAST_NAME;

"""3"""
SELECT SUM(SALARY)
FROM pds.employees;

"""4"""
SELECT MAX(SALARY), MIN(SALARY)
FROM pds.employees;

"""5"""
SELECT AVG(SALARY), count(EMPLOYEE_ID)
FROM pds.employees;
