# Write your MySQL query statement below
select e1.name
from Employee as e1 #manage 
join Employee as e2 #all 
on e1.id = e2.managerId 
group by e1.id 
having count(e1.id)>=5
