-- SQL Queries för Electronics Shop

-- Grundläggande queries

-- 1. Alla produkter sorterade efter namn
SELECT
    id,
    name,
    category,
    price,
    stock_quantity
FROM products
ORDER BY name ASC;

-- 2. Produkter som kostar mer än 5000 kr
SELECT
    id,
    name,
    price,
    category,
    brand_id
FROM products
WHERE price > 5000
ORDER BY price DESC;

-- 3. Beställningar från 2024
SELECT
    id,
    customer_id,
    order_date,
    total_amount,
    status
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2024
ORDER BY order_date DESC;

-- 4. Pending beställningar
SELECT
    id,
    customer_id,
    order_date,
    total_amount,
    shipping_city
FROM orders
WHERE status = 'pending'
ORDER BY order_date;

-- JOIN-queries

-- 5. Produkter med tillverkares namn
SELECT
    p.id,
    p.name AS product_name,
    b.name AS brand_name,
    p.category,
    p.price
FROM products AS p
INNER JOIN brands AS b ON p.brand_id = b.id
ORDER BY b.name, p.name;

-- 6. Beställningar med kundens namn och belopp
SELECT
    o.id AS order_id,
    o.order_date,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    o.total_amount,
    o.status
FROM orders AS o
INNER JOIN customers AS c ON o.customer_id = c.id
ORDER BY o.order_date DESC;

-- 7. Vilka produkter varje kund har köpt
SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    p.name AS product_name,
    oi.quantity,
    oi.unit_price,
    o.order_date
FROM customers AS c
INNER JOIN orders AS o ON o.customer_id = c.id
INNER JOIN order_items AS oi ON oi.order_id = o.id
INNER JOIN products AS p ON p.id = oi.product_id
ORDER BY customer_name, o.order_date DESC;

-- Aggregering och analys

-- 8. Antal produkter per tillverkare
SELECT
    b.name AS brand_name,
    COUNT(p.id) AS product_count,
    SUM(p.stock_quantity) AS total_stock
FROM brands AS b
LEFT JOIN products AS p ON p.brand_id = b.id
GROUP BY b.name
ORDER BY product_count DESC, brand_name;

-- 9. Kunder som har spenderat mest totalt
SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    SUM(o.total_amount) AS total_spending,
    COUNT(o.id) AS order_count
FROM customers AS c
INNER JOIN orders AS o ON o.customer_id = c.id
WHERE o.status = 'completed'
GROUP BY c.id, customer_name
ORDER BY total_spending DESC
LIMIT 5;

-- 10. Produkter med genomsnittligt betyg
SELECT
    p.name AS product_name,
    p.category,
    ROUND(AVG(r.rating), 2) AS average_rating,
    COUNT(r.id) AS review_count
FROM products AS p
LEFT JOIN reviews AS r ON r.product_id = p.id
GROUP BY p.id, p.name, p.category
HAVING COUNT(r.id) > 0
ORDER BY average_rating DESC, review_count DESC;

