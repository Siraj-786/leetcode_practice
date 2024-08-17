# Write your MySQL query statement below
select t.id as product_id,if(t.new_c is not null,round(t.new_c/t.s,2),0) as average_price
from 
(select p.product_id as id,sum(p.price*u.units) as new_c,sum(u.units) as s 
from Prices as p
left join UnitsSold as u
on p.product_id=u.product_id and p.start_date<=u.purchase_date and p.end_date>=u.purchase_date
group by p.product_id) as t;