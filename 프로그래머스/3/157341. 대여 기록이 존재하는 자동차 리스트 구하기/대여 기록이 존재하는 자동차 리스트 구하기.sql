-- 코드를 입력하세요
SELECT distinct a.car_id from car_rental_company_car as a
inner join car_rental_company_rental_history as b on a.car_id = b.car_id
where a.car_type = '세단' and month(start_date) = '10'
order by a.car_id desc