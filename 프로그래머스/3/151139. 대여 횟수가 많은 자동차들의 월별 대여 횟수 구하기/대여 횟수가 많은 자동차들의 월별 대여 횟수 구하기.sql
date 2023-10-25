-- 코드를 입력하세요
#MONTH	CAR_ID	RECORDS
# 1. 기간내 추출 2. 월 추출
SELECT month(start_date) as month, car_id, count(history_id) as records
from car_rental_company_rental_history
where car_id in (
    select car_id 
    from car_rental_company_rental_history 
    where start_date between '2022-08-01' and '2022-10-31' 
    group by car_id 
    having count(car_id)>=5) and START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
group by month,car_id
HAVING COUNT(*) <> 0
order by month, car_id desc