# Write your MySQL query statement belows
select sell_date,
count(distinct(product)) as num_sold ,
group_concat(distinct product ORDER BY product separator ",") AS products
from activities 
group by sell_date  
