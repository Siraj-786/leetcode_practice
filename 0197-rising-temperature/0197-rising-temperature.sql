# Write your MySQL query statement below
select t.id 
from Weather as w left join Weather as t
on date_add(w.recordDate,interval 1 day)=t.recordDate
where w.temperature<t.temperature
;

