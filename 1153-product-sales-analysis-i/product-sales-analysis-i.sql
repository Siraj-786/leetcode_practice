# Write your MySQL query statement below
select product_name ,year  ,price
from sales s 
left join Product 
using(product_id )
