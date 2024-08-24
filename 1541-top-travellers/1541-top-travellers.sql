# Write your MySQL query statement below
select  t.name,if(sum(t.d) is not null,sum(t.d),0) as travelled_distance 
from (select  Users.id,Users.name,Rides.distance as d
from Users 
left join Rides
on Users.id=Rides.user_id) as t 
group by t.id
order by travelled_distance desc,name;