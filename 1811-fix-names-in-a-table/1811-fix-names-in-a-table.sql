# Write your MySQL query statement below
-- select user_id,group_concat(upper(left(name,1)),len()) as u 
select user_id,concat(upper(left(name,1)),lower(right(name,length(name)-1))) as name
from Users
order by user_id;

