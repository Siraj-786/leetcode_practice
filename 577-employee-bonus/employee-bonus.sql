# Write your MySQL query statement below

select name,bonus  from employee  e
left join Bonus  b
using(empId )
where bonus <1000 or b.empId is null