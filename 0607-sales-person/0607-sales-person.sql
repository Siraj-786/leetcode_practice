# Write your MySQL query statement below




-- select * 
-- from SalesPerson
-- where sales_id in (1,2,3);


select name 
from SalesPerson
where sales_id not in (
select o.sales_id 
from Orders as o
left join Company as c
on o.com_id=c.com_id
where c.name='RED') ;

