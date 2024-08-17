select r.contest_id,round((count(u.user_id)/(select count(user_id) from Users))*100,2) as percentage
from Users as u 
left join Register as r 
on u.user_id=r.user_id
where contest_id is not null
group by r.contest_id

order by percentage desc,contest_id asc ;
;