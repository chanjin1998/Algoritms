-- 코드를 입력하세요
# 판매량(c.sales) * 판매가(a.price)
SELECT a.author_id, b.author_name, a.category,sum(c.sales*a.price) as totla_sales from book as a
inner join author as b on a.author_id = b.author_id
inner join book_sales as c on a.book_id = c.book_id
where sales_date like '2022-01%'
group by a.author_id, category
order by a.author_id, category desc