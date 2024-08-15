# Write your MySQL query statement below

#select a.id,a. name,a. department,a. managerId
select t.name from
(select e.id,e.name,f.managerId as man
from Employee as e 
left join Employee as f 
on e.id=f.managerID 
where f.managerID is not null ) as t 
group by t.id,t.name
having count(t.man)>4;