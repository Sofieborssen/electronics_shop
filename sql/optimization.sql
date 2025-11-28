-- Database Optimization

-- Query 2: Produkter dyrare än 5000 kr
-- Utan index på price måste PostgreSQL skanna hela tabellen sekventiellt.
-- Ett index gör att Index Scan kan användas istället.

-- Före optimering:
-- EXPLAIN ANALYZE
-- SELECT id, name, price, category
-- FROM products
-- WHERE price > 5000
-- ORDER BY price DESC;
-- Resultat: Seq Scan on products

CREATE INDEX IF NOT EXISTS idx_products_price ON products (price);

-- Efter optimering:
-- EXPLAIN ANALYZE
-- SELECT id, name, price, category
-- FROM products
-- WHERE price > 5000
-- ORDER BY price DESC;
-- Resultat: Index Scan using idx_products_price

-- Query 9: Kunder som har spenderat mest totalt
-- Filtrerar på status = 'completed' och grupperar per kund.
-- Partiellt index på completed orders gör grupperingen snabbare.

-- Före optimering:
-- EXPLAIN ANALYZE
-- SELECT
--     CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
--     SUM(o.total_amount) AS total_spending
-- FROM customers AS c
-- INNER JOIN orders AS o ON o.customer_id = c.id
-- WHERE o.status = 'completed'
-- GROUP BY customer_name
-- ORDER BY total_spending DESC
-- LIMIT 5;
-- Resultat: Seq Scan on orders

CREATE INDEX IF NOT EXISTS idx_orders_completed_customer_amount
    ON orders (customer_id, total_amount)
    WHERE status = 'completed';

-- Efter optimering:
-- EXPLAIN ANALYZE
-- SELECT
--     CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
--     SUM(o.total_amount) AS total_spending
-- FROM customers AS c
-- INNER JOIN orders AS o ON o.customer_id = c.id
-- WHERE o.status = 'completed'
-- GROUP BY customer_name
-- ORDER BY total_spending DESC
-- LIMIT 5;
-- Resultat: Bitmap Index Scan on idx_orders_completed_customer_amount

