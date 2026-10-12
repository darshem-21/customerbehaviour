https://colab.research.google.com/drive/10t6xdUHD4_UOl_E4QS3sdF-TcxGsXTLY?usp=sharing

//*sql
  select * from customer limit 20

select gender , SUM(purchase_amount) as revenue
from customer
group by gender

select  customer_id,purchase_amount
from customer
where discount_applied = 'Yes' and purchase_amount >= (SELECT AVG(purchase_amount) from customer)

select item_purchased,ROUND(AVG(review_rating::NUMERIC),2) as "Average Poduct Rating"
from customer
GROUP by item_purchased
ORDER by AVG(review_rating) DESC
limit 5;

SELECT shipping_type,ROUND(AVG(purchase_amount),2)
from customer
where shipping_type in ('Standard','Express')
group by shipping_type

select subscription_status,COUNT(customer_id) as total_customer,
  ROUND(AVG(purchase_amount),2) as avg_spend,
  ROUND(sum(purchase_amount),2) as total_revenue
from customer
group by subscription_status
order by total_revenue, avg_spend desc;

SELECT item_purchased,
       ROUND(100.0 * SUM(CASE WHEN discount_applied = 'Yes' THEN 1 ELSE 0 END)/COUNT(*),2) AS discount_rate
FROM customer
GROUP BY item_purchased
ORDER BY discount_rate DESC
LIMIT 5;

with customer_type as (
SELECT customer_id, previous_purchases,
CASE 
    WHEN previous_purchases = 1 THEN 'New'
    WHEN previous_purchases BETWEEN 2 AND 10 THEN 'Returning'
    ELSE 'Loyal'
    END AS customer_segment
FROM customer)

select customer_segment,count(*) AS "Number of Customers" 
from customer_type 
group by customer_segment;


WITH item_counts AS (
    SELECT category,
           item_purchased,
           COUNT(customer_id) AS total_orders,
           ROW_NUMBER() OVER (PARTITION BY category ORDER BY COUNT(customer_id) DESC) AS item_rank
    FROM customer
    GROUP BY category, item_purchased
)
SELECT item_rank,category, item_purchased, total_orders
FROM item_counts
WHERE item_rank <=3;

SELECT subscription_status,
       COUNT(customer_id) AS repeat_buyers
FROM customer
WHERE previous_purchases > 5
GROUP BY subscription_status;

SELECT 
    age_group,
    SUM(purchase_amount) AS total_revenue
FROM customer
GROUP BY age_group
ORDER BY total_revenue desc;

SELECT *
FROM public.customer;
*//

https://datastudio.google.com/reporting/9b91d111-e1d2-4a38-9aa8-86180dc64076
