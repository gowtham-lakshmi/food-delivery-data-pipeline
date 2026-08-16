SELECT * FROM food_delivery_db.public.orders;
select count(*) as total_orders from food_delivery_db.public.orders;
select sum(order_amount) as total_revenue from food_delivery_db.public.orders;

select city, count(*) as order_count
from food_delivery_db.public.orders
group by city
order by order_count desc;

select cuisine_type, avg(delivery_time_mins) as avg_delivery_time
from food_delivery_db.public.orders
group by cuisine_type;

select * from food_delivery_db.public.orders
where delivery_status = 'Cancelled';

select * from food_delivery_db.public.orders
where order_amount > (select avg(order_amount) from food_delivery_db.public.orders);

select order_id, restaurant_name, order_amount
from food_delivery_db.public.orders
order by order_amount desc
limit 5;

