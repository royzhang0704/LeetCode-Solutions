# Write your MySQL query statement below
with first_order_info as (
    select 
    customer_id,
    min(order_date) as first_order_date
    from
    Delivery
    group by 
    customer_id
)

select round(sum(case when d.order_date=d.customer_pref_delivery_date then 1 else 0 end )*100/count(*),2)
as immediate_percentage
from first_order_info f
join Delivery d
on f.customer_id=d.customer_id
and f.first_order_date=d.order_date
