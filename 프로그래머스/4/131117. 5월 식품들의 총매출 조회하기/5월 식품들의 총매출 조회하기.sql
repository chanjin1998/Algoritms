-- 코드를 입력하세요
SELECT b.product_id, product_name,sum(amount*price) as total_sales from food_product as a inner join food_order as b 
on a.product_id = b.product_id
where produce_date like '2022-05%'
group by b.product_id
order by total_sales desc, b.product_id
