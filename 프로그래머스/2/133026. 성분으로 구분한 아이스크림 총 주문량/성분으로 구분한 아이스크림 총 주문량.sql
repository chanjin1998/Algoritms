select ingredient_type, sum(total_order) as total_order from first_half as fh join icecream_info as ii
on fh.flavor = ii.flavor
group by ingredient_type
order by total_order