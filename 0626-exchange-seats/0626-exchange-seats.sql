# Write your MySQL query statement below
select s1.id as id ,if(s2.id is not null,s2.student,s1.student) as student from 
    Seat as s1 
    left join 
    Seat as s2 
    on (s1.id+1=s2.id and s1.id&1=1 and s2.id&1<>1) or (s1.id=s2.id+1 and s2.id&1=1 and s1.id&1<>1);

