-- 코드를 입력하세요
SELECT b.user_id, nickname,concat(city,' ',street_address1,' ',street_address2)as 전체주소, 
concat(LEFT(tlno,3), '-', MID(tlno,4,4),'-', RIGHT(tlno,4)) AS 전화번호 
from used_goods_board as a
inner join used_goods_user as b on a.writer_id = b.user_id
group by writer_id
having count(writer_id)>=3
order by b.user_id desc