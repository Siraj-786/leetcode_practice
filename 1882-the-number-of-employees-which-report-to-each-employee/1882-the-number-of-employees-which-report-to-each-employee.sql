# Write your MySQL query statement below
select e1.employee_id,e1.name,count(e2.reports_to) as reports_count,round(avg(e2.age)) as average_age from 
Employees as e1 
left join Employees as e2 
on e1.employee_id=e2.reports_to
group by e1.employee_id
having average_age is not null
order by e1.employee_id ;