# Write your MySQL query statement below
select min(t1.name) as results   from (
select u.name,count(distinct movie_id) as no_of from 
    MovieRating as m 
    left join 
    Users as u 
    on m.user_id=u.user_id
    group by m.user_id
    order by no_of) as t1
    where t1.no_of=(select max(no_of) from (select u.name,count(distinct movie_id) as no_of from 
    MovieRating as m 
    left join 
    Users as u 
    on m.user_id=u.user_id
    group by m.user_id
    order by no_of) as t1)

union  all

select t.t1 as results from 
(select avg(m1.rating) as av,m2.title as t1  from 
    MovieRating as m1
    left join 
    Movies as m2 
    on m1.movie_id=m2.movie_id 
    where m1.created_at between '2020-02-01' and '2020-02-29'
    group by m1.movie_id
    order by av desc,t1 
    limit 1) as t;



