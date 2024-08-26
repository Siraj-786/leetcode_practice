# Write your MySQL query statement below

# someone else solution \U0001f97a
SELECT 
    'Low Salary' AS category,
    SUM(income < 20000) AS accounts_count
FROM 
    Accounts

UNION 

    SELECT 
        'Average Salary' AS category,
        SUM(income BETWEEN 20000 AND 50000 ) AS accounts_count
    FROM 
        Accounts

UNION

    SELECT 
        'High Salary' AS category,
        sum(income > 50000) AS accounts_count
    FROM 
        Accounts;