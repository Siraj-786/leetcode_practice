# Write your MySQL query statement below
-- select l1.id as a,l1.num as n1 
select distinct t.num as  ConsecutiveNums from (select * from (
    select l1.id as a,l1.num as n1,l2.id as b,l2.num as n2
    from Logs as l1 
    left join Logs as l2 
    on l1.id=(l2.id-1) and l1.num=l2.num
    having n2 is not null) as l3
left join Logs as l4 
on l3.b=(l4.id-1) and l3.n2=l4.num
having l4.id is not null)as t
;