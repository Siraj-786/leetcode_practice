select case 
    when (select max(salary) from Employee)=salary then  null
    else salary
    end as SecondHighestSalary
from Employee
order by SecondHighestSalary desc
limit 1;

-- SELECT   
--     CASE   
--         WHEN salary = (SELECT MAX(salary) FROM Employee) THEN salary - 10000  
--         ELSE salary   
--     END AS new_salary  
-- FROM Employee;