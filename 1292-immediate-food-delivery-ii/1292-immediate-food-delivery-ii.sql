# Write your MySQL query statement below
select round(sum(t.p=t.q)/count(t.p)*100,2) as immediate_percentage
from 
(select min(order_date) as p,min(customer_pref_delivery_date) as q
from Delivery

group by customer_id)as t;
