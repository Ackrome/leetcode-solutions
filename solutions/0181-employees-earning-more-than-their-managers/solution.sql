# Write your MySQL query statement below
SELECT E.name as 'Employee' FROM (SELECT 
    e.id, 
    e.name, 
    e.salary, 
    e.managerId, 
    m.salary AS managerSalary
FROM 
    Employee  e
LEFT JOIN 
    Employee  m ON e.managerId = m.id) E WHERE E.salary > E.managerSalary
