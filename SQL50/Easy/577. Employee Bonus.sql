# Write your MySQL query statement below
select name,ifnull(bonus,null) as bonus
from
Employee
left join 
Bonus
on Employee.empId=Bonus.empId
where 
bonus<1000 or bonus is null;
