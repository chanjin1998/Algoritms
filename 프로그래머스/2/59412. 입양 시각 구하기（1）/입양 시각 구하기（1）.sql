select hour(datetime) as hour, count(animal_id) as count from animal_outs
where hour(datetime) >= 9 and hour(datetime) <=19
group by hour
order by hour