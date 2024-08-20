select customer_number
from Orders
group by customer_number
having count(customer_number)=
(select
max(c) from 
(select count(customer_number) as c
from Orders
group by customer_number) as sub);
-- 

-- SELECT customer_number  
-- FROM Orders  
-- GROUP BY customer_number  
-- HAVING COUNT(customer_number) = (SELECT MAX(c) FROM (SELECT COUNT(customer_number) AS c FROM Orders GROUP BY customer_number) AS subquery);