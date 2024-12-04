select round(sum(order_date = customer_pref_delivery_date)/count(*) * 100, 2) as immediate_percentage
from
(
select *
,row_number() over(partition by customer_id order by order_date asc) as rn
from Delivery
)I
where rn = 1