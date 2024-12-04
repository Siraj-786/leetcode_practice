# Write your MySQL query statement below

select contest_id,
round(count(user_id)*100/(select count(user_id) from  users),2) as percentage
from register r 
left join users u 
using(user_id)
group by contest_id
order by percentage desc,contest_id