# Write your MySQL query statement below


select a.product_id ,a.product_name
from Product as a 
left join Sales as s 
on a.product_id=s.product_id
group by product_id
having (min(sale_date) between '2019-01-01' and '2019-03-31') and (max(sale_date) between '2019-01-01' and '2019-03-31');
