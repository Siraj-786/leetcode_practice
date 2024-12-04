# Write your MySQL query statement below

select activity_date as day, count(distinct user_id) active_users 
from activity 
where activity_date between DATE('2019-07-27') - INTERVAL '29' DAY AND DATE('2019-07-27')
group by 1 
having count(distinct user_id)>=1