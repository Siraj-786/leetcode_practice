# Write your MySQL query statement below

select class
from courses c
group by class
having count(student) >4
