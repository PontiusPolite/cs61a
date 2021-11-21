.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) FROM inventory GROUP BY item;


CREATE TABLE shopping_list_prices AS
  SELECT lp.item, lp.store, min(p.MSRP / p.rating) FROM lowest_prices as lp, products as p
    WHERE lp.item = p.name
    GROUP BY p.category ORDER BY lp.item;

CREATE TABLE shopping_list AS
  SELECT item, store FROM shopping_list_prices;


CREATE TABLE total_bandwidth AS
  SELECT sum(s.Mbs) FROM stores as s, shopping_list as p where p.store = s.store;

