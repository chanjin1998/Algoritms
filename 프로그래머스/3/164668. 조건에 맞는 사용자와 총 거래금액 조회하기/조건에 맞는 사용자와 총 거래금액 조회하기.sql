-- 코드를 입력하세요
#총금액이 70만 원 이상인 사람의 회원 ID, 닉네임, 총거래금액
SELECT user_id, b.nickname, sum(price) as total_sales from used_goods_board as a
left join used_goods_user as b on a.writer_id = b.user_id
where status = 'DONE'
group by user_id
having total_sales >= 700000
order by total_sales