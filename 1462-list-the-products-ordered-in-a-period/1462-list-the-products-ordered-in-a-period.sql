# Write your MySQL query statement below
select t.product_name,sum(t.unit)as unit from 
(select  Products.product_id,Products.product_name,Orders.unit
from Products
left join Orders
on Products.product_id=Orders.product_id
where '2020-02-01'<=order_date and order_date<='2020-02-29') as t

group by t.product_id
having sum(t.unit)>=100;

