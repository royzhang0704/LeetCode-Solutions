# Write your MySQL query statement below
select today.id
from weather as today
left join weather as yesterday
on  datediff(today.recordDate,yesterday.recordDate)=1
where today.temperature>yesterday.temperature


"""
先自己join 自己並且只要日期相差一天的 <- 為join條件
之後再找出當前日期溫度比前一天溫度高的
"""
