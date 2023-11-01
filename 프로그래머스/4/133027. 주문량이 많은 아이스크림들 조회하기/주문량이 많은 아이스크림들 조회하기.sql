-- 코드를 입력하세요
SELECT a.flavor from first_half as a inner join july as b 
on a.flavor = b.flavor
group by a.flavor
order by (sum(distinct a.total_order)+sum(distinct b.total_order)) desc
limit 3