-- 코드를 입력하세요
SELECT BOARD_ID,WRITER_ID,TITLE,PRICE,
(case when board_id in 
(select board_id from used_goods_board
where status = 'sale') then '판매중'
when board_id in 
(select board_id from used_goods_board
where status = 'reserved') then '예약중'
else '거래완료'end) as status
from used_goods_board
where created_date = '2022-10-05'
order by board_id desc