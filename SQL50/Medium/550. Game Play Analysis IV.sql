# Write your MySQL query statement below
select round(avg(a.event_date is not null),2) fraction
from
    (select player_id,min(event_date) as login
    from activity
    group by player_id ) p
left join activity a 
on p.player_id=a.player_id and datediff(a.event_date,p.login)=1
