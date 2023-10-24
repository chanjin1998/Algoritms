-- 코드를 입력하세요
# 즐겨찾기수가 가장 많은 식당
SELECT food_type, rest_id, rest_name, favorites from rest_info
where favorites in (select max(favorites) from rest_info group by food_type)
group by food_type
order by food_type desc