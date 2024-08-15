# Write your MySQL query statement below
select a.student_id ,a.student_name,s.subject_name,count(e.subject_name) as attended_exams
from Students as a 
cross join Subjects as s 

left join Examinations as e 
on a.student_id=e.student_id and s.subject_name=e.subject_name
group by a.student_id,a.student_name,s.subject_name
order by a.student_id,s.subject_name;
