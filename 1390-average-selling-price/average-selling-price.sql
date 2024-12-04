# Write your MySQL query statement below


select p.product_id , IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) as average_price
from prices p 
left join unitssold s
on p.product_id=s.product_id
and s.purchase_date BETWEEN start_date AND end_date
group by product_id