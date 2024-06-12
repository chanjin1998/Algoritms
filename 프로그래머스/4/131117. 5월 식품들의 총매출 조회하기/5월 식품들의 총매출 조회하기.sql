select a.product_id, product_name, sum(price*amount) as total_sales from food_product a join food_order b on a.product_id = b.product_id
where produce_date like "2022-05%"
group by b.product_id
order by total_sales desc, b.product_id