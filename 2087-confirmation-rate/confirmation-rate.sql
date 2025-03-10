# Write your MySQL query statement below

select s.user_id,
round(SUM(CASE WHEN action="confirmed" then 1 else 0 end)*1.0/count(*),2) as confirmation_rate 
 from signups  s
left join confirmations c 
on s.user_id=c.user_id
group by 1