-- Avancerade SQL Queries (VG-nivå)

-- Subqueries

-- 1. Produkter vars pris är högre än genomsnittspriset
SELECT
    id,
    name,
    price,
    category,
    (SELECT AVG(price) FROM products) AS average_price
FROM products
WHERE price > (
    SELECT AVG(price) FROM products
)
ORDER BY price DESC;

-- 2. Kunder som har beställt fler än genomsnittligt antal beställningar
SELECT
    c.id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email,
    COUNT(o.id) AS order_count
FROM customers AS c
INNER JOIN orders AS o ON o.customer_id = c.id
GROUP BY c.id, customer_name, c.email
HAVING COUNT(o.id) > (
    SELECT AVG(order_count)
    FROM (
        SELECT COUNT(*) AS order_count
        FROM orders
        GROUP BY customer_id
    ) AS customer_orders
)
ORDER BY order_count DESC;

-- Window functions

-- 3. Ranka produkter per tillverkare baserat på pris
SELECT
    b.name AS brand_name,
    p.name AS product_name,
    p.price,
    ROW_NUMBER() OVER (
        PARTITION BY b.id
        ORDER BY p.price DESC
    ) AS price_rank_within_brand
FROM products AS p
INNER JOIN brands AS b ON p.brand_id = b.id
ORDER BY brand_name, price_rank_within_brand;

-- 4. Kunders totala spending och rank
SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(o.total_amount) AS total_spending,
    COUNT(o.id) AS order_count,
    RANK() OVER (
        ORDER BY SUM(o.total_amount) DESC
    ) AS spending_rank
FROM customers AS c
INNER JOIN orders AS o ON o.customer_id = c.id
WHERE o.status = 'completed'
GROUP BY c.id, customer_name
ORDER BY spending_rank;

-- CASE och villkorlig logik

-- 5. Kategorisera produkter: Budget (<1000), Medium (1000-5000), Premium (>5000)
SELECT
    id,
    name,
    price,
    category,
    CASE
        WHEN price < 1000 THEN 'Budget'
        WHEN price BETWEEN 1000 AND 5000 THEN 'Medium'
        ELSE 'Premium'
    END AS price_segment
FROM products
ORDER BY price DESC;

-- 6. Kategorisera kunder: VIP (>3), Regular (2-3), New (1)
SELECT
    c.id,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email,
    COUNT(o.id) AS order_count,
    CASE
        WHEN COUNT(o.id) > 3 THEN 'VIP'
        WHEN COUNT(o.id) BETWEEN 2 AND 3 THEN 'Regular'
        WHEN COUNT(o.id) = 1 THEN 'New'
        ELSE 'Prospect'
    END AS customer_segment
FROM customers AS c
LEFT JOIN orders AS o ON o.customer_id = c.id
GROUP BY c.id, customer_name, c.email
ORDER BY order_count DESC, customer_name;

