# Write your MySQL query statement below
select customer_id ,count(v.visit_id)count_no_trans 
from visits v 
left join Transactions t
on v.visit_id=t.visit_id
where t.visit_id is null
group by 1