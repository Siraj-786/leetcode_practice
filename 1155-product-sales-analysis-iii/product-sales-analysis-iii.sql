# Write your MySQL query statement below

select product_id, year as first_year, quantity, price from (
select  product_id, year, quantity, price,
min(year) over(partition by product_id) as first_year
from product p
join  Sales s
using(product_id )
)x where first_year=year