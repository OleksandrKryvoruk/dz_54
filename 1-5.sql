"""1"""
select count(JOB_ID) from pds.employees;

"""2"""
SELECT AVG(SALARY) as AVG_SALARY, count(EMPLOYEE_ID) as NUM_STUFF_90 from pds.employees
where DEPARTMENT_ID = 90;

"""3"""
SELECT JOB_ID, count(JOB_ID) from pds.employees
group by JOB_ID;

"""4"""
SELECT * from pds.employees right join pds.departments
on pds.employees.DEPARTMENT_ID = pds.departments.DEPARTMENT_ID;

"""5"""
SELECT * from pds.employees left join pds.departments
on pds.employees.DEPARTMENT_ID = pds.departments.DEPARTMENT_ID
where LOCATION_ID = 2400;
