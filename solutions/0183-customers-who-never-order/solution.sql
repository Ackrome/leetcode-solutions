# Write your MySQL query statement below C.name as 'Customers'
SELECT C.name as 'Customers' FROM Customers C LEFT OUTER JOIN Orders O ON C.id = O.customerId WHERE O.customerId is NULL
