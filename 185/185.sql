

-- https://leetcode.com/problems/department-top-three-salaries/description/

with
t_uniq as (
    select salary, departmentId from Employee group by 1,2
),
t_ranked as (
    select *, row_number() over (partition by departmentid order by salary desc) r from t_uniq
),
t_thirds as (
    select departmentId, salary from t_ranked where r <= 3
),
t_limit as (
    select departmentId, min(salary) as salary_limit from t_thirds group by departmentId
),
t_ppl as (
    select e.id from Employee e join t_limit t on e.departmentId=t.departmentId
    where e.salary >= t.salary_limit
)
select 
    d.name as "Department",
    e.name as "Employee",
    e.salary as "Salary"
from Employee e join Department d on e.departmentId=d.id
where e.id in (select id from t_ppl)

