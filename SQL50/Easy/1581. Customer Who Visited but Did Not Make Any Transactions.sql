# Write your MySQL query statement below
select customer_id,count(*)as count_no_trans
from
Visits left join Transactions
on Visits.visit_id =Transactions.visit_id 
where Transaction_id is null
group by customer_id 


"""
要找出去參訪但沒有交易的客戶id 以及沒交易的數量

先去join visit_id 的交易為null 的找出來 但有可能有重複的user 要做group
"""
