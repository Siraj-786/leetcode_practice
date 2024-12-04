# Write your MySQL query statement below
SELECT customer_id from Customer GROUP BY customer_id HAVING(count(distinct(product_key))) = (SELECT count(product_key) from Product)
#SELECT customer_id, count(product_key) from Customer GROUP BY customer_id;
#SELECT count(product_key) from Product;