# Write your MySQL query statement below
select ifnull(unique_id,null) as unique_id,name from Employees left join EmployeeUNI on Employees.id=EmployeeUNI.id 
