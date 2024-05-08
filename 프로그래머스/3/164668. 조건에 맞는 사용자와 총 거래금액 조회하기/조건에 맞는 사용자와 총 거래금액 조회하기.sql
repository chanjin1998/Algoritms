select user_id, nickname, sum(price) as price
from used_goods_board as ugb join used_goods_user as ugu 
on ugb.writer_id = ugu.user_id
where status = 'done'
group by user_id
having price >= 700000
order by price
