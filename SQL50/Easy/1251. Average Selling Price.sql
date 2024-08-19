select
    combined.product_id,
    ifnull(round(sum(combined.units * combined.price) / sum(combined.units), 2),0) AS average_price
from (
    select 
        p.product_id, 
        u.units, 
        p.price
    from prices p
    left join  unitssold u
    on p.product_id = u.product_id
    and u.purchase_date between p.start_date and  p.end_date
) as combined
group by combined.product_id;
