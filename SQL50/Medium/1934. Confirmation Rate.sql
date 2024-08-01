# Write your MySQL query statement below
select Signups.user_id,ifnull(round(avg(action="confirmed"),2),0) as Confirmation_rate
from Signups left join Confirmations
on Signups.user_id=Confirmations.user_id
group by Signups.user_id
