-- Testdata för Electronics Shop
-- Kör efter schema.sql

BEGIN;

-- Brands
INSERT INTO brands (id, name, country, founded_year, description)
VALUES
    (1, 'Apple', 'USA', 1976, 'Amerikansk teknologikoncern känd för iPhone, iPad och Mac.'),
    (2, 'Samsung', 'South Korea', 1938, 'Sydkoreansk elektroniktillverkare, världsledande inom smartphones och TV-apparater.'),
    (3, 'Sony', 'Japan', 1946, 'Japansk multinationell konglomerat, känd för PlayStation, TV och ljudprodukter.');

-- Products
INSERT INTO products (id, name, brand_id, sku, release_year, price, warranty_months, category, stock_quantity)
VALUES
    -- Apple produkter
    (1, 'iPhone 15 Pro', 1, 'APP-IP15P-256', 2023, 12990.00, 12, 'Smartphones', 45),
    (2, 'iPhone 14', 1, 'APP-IP14-128', 2022, 8990.00, 12, 'Smartphones', 60),
    (3, 'MacBook Pro 14"', 1, 'APP-MBP14-M3', 2023, 19990.00, 12, 'Laptops', 25),
    (4, 'iPad Air', 1, 'APP-IPAD-AIR', 2022, 6990.00, 12, 'Tablets', 40),
    (5, 'AirPods Pro', 1, 'APP-AIRPODS-PRO', 2023, 3290.00, 12, 'Audio', 80),
    
    -- Samsung produkter
    (6, 'Galaxy S24 Ultra', 2, 'SAM-GS24U-256', 2024, 13990.00, 24, 'Smartphones', 35),
    (7, 'Galaxy Tab S9', 2, 'SAM-TABS9-128', 2023, 8990.00, 24, 'Tablets', 30),
    (8, 'Samsung 55" QLED TV', 2, 'SAM-Q55-2024', 2024, 12990.00, 24, 'TV', 20),
    (9, 'Galaxy Watch 6', 2, 'SAM-GW6-44', 2023, 3990.00, 24, 'Wearables', 50),
    
    -- Sony produkter
    (10, 'PlayStation 5', 3, 'SONY-PS5-DISC', 2020, 5990.00, 24, 'Gaming', 15),
    (11, 'Sony WH-1000XM5', 3, 'SONY-WH1000XM5', 2022, 4490.00, 24, 'Audio', 40),
    (12, 'Sony 65" OLED TV', 3, 'SONY-A65-2023', 2023, 19990.00, 24, 'TV', 12);

-- Customers
INSERT INTO customers (id, first_name, last_name, email, phone, city, registration_date)
VALUES
    (1, 'Anna', 'Andersson', 'anna.andersson@example.com', '+46-70-1234567', 'Stockholm', '2023-01-15'),
    (2, 'Erik', 'Berg', 'erik.berg@example.com', '+46-73-2345678', 'Göteborg', '2023-03-20'),
    (3, 'Maria', 'Carlsson', 'maria.carlsson@example.com', '+46-72-3456789', 'Malmö', '2023-05-10'),
    (4, 'Johan', 'Dahl', 'johan.dahl@example.com', '+46-70-4567890', 'Uppsala', '2024-02-14'),
    (5, 'Sara', 'Eriksson', 'sara.eriksson@example.com', '+46-76-5678901', 'Stockholm', '2024-06-08');

-- Orders
INSERT INTO orders (id, customer_id, order_date, total_amount, status, shipping_city)
VALUES
    -- Gamla beställningar (2023)
    (1, 1, '2023-06-15', 12990.00, 'completed', 'Stockholm'),
    (2, 2, '2023-08-22', 8990.00, 'completed', 'Göteborg'),
    (3, 3, '2023-09-10', 6990.00, 'completed', 'Malmö'),
    (4, 1, '2023-11-05', 3290.00, 'completed', 'Stockholm'),
    (5, 2, '2023-12-18', 13990.00, 'completed', 'Göteborg'),
    
    -- Nya beställningar (2024)
    (6, 4, '2024-01-20', 19990.00, 'completed', 'Uppsala'),
    (7, 5, '2024-03-12', 4490.00, 'completed', 'Stockholm'),
    (8, 1, '2024-05-08', 5990.00, 'pending', 'Stockholm'),
    (9, 3, '2024-07-15', 12990.00, 'pending', 'Malmö'),
    (10, 2, '2024-09-22', 8990.00, 'completed', 'Göteborg');

-- Order_Items
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES
    (1, 1, 1, 12990.00),  -- iPhone 15 Pro
    (2, 2, 1, 8990.00),   -- iPhone 14
    (3, 4, 1, 6990.00),   -- iPad Air
    (4, 5, 1, 3290.00),   -- AirPods Pro
    (5, 6, 1, 13990.00),  -- Galaxy S24 Ultra
    (6, 3, 1, 19990.00),  -- MacBook Pro
    (7, 11, 1, 4490.00),  -- Sony WH-1000XM5
    (8, 10, 1, 5990.00),  -- PlayStation 5
    (9, 8, 1, 12990.00),  -- Samsung QLED TV
    (10, 7, 1, 8990.00);

-- Reviews
INSERT INTO reviews (product_id, customer_id, rating, comment, review_date)
VALUES
    (1, 1, 5, 'Fantastisk telefon! Kameran är otrolig och batteriet håller länge.', '2023-07-01'),
    (2, 2, 4, 'Bra telefon för priset. Lite gammal modell men fungerar utmärkt.', '2023-09-15'),
    (3, 4, 5, 'Bästa laptopen jag ägt. Snabb och kraftfull.', '2024-02-10'),
    (4, 3, 4, 'Perfekt för läsning och streaming. Lätt och smidig.', '2023-10-05'),
    (5, 1, 5, 'Bästa hörlurarna! Brusreduceringen är magisk.', '2023-12-20'),
    (6, 2, 5, 'Utmärkt telefon med fantastisk kamera och långt batteri.', '2024-01-25'),
    (7, 3, 4, 'Bra surfplatta, perfekt storlek för resor.', '2024-02-15'),
    (8, 1, 5, 'Fantastisk bildkvalitet! Rekommenderas starkt.', '2024-08-01'),
    (10, 4, 5, 'Bästa konsolen! Grafiken är otrolig.', '2024-06-01'),
    (11, 5, 5, 'Perfekta hörlurar med utmärkt ljudkvalitet.', '2024-04-20');

-- Återställ sekvenser
SELECT setval('brands_id_seq', (SELECT MAX(id) FROM brands));
SELECT setval('products_id_seq', (SELECT MAX(id) FROM products));
SELECT setval('customers_id_seq', (SELECT MAX(id) FROM customers));
SELECT setval('orders_id_seq', (SELECT MAX(id) FROM orders));
SELECT setval('order_items_id_seq', (SELECT MAX(id) FROM order_items));
SELECT setval('reviews_id_seq', (SELECT MAX(id) FROM reviews));

COMMIT;

