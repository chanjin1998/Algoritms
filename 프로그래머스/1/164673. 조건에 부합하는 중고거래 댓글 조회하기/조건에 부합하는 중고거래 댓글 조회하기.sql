-- 코드를 입력하세요
SELECT a.title,a.board_id,b.reply_id,b.writer_id,b.contents,date_format(b.created_date,'%Y-%m-%d') as created_date
from used_goods_board as a 
inner join used_goods_reply as b 
on a.board_id = b.board_id
where month(a.created_date) = 10
order by b.created_date asc, a.title asc