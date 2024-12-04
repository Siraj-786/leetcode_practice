# Write your MySQL query statement below

select 
e.reports_to as employee_id ,m.name, count(distinct e.employee_id)as reports_count ,
round(avg(e.age) )as average_age 
from employees e
join employees m
on e.reports_to =m.employee_id
where e.reports_to is not null
group by 1,2