-- 코드를 입력하세요
select month(start_date) month, car_id, count(car_id)
from car_rental_company_rental_history
where car_id in
(select car_id from car_rental_company_rental_history
where start_date between "2022-08-01" and "2022-10-31"
 group by car_id
 having count(car_id) >=5 and START_DATE BETWEEN '2022-08-01' AND '2022-10-31'

)
group by month, car_id
having count(car_id)>0
order by month, car_id desc