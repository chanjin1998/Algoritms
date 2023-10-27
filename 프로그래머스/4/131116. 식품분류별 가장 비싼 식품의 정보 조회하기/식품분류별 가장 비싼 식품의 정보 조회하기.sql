select category,max(price) as max_price,product_name from food_product
where price in (select max(price) from food_product group by category)
group by category
having category in ('과자','국','김치','식용유')
order by max_price desc


#각 카테고리별 최고가 = 카테고리별로 그룹화 최고가 추려