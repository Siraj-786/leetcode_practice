# Write your MySQL query statement below
select unique_id as unique_id,name from 
employees e
left join  EmployeeUNI u 
on u.id = e.id