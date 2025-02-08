# Write your MySQL query statement below

select  s.student_id , s.student_name,sb.subject_name,
count(e.student_id ) as attended_exams 
from students s
CROSS JOIN Subjects sb 
LEFT JOIN Examinations e
on e.student_id  =s.student_id 
AND e.subject_name = sb.subject_name


group by 1,2,3
order by student_id , subject_name