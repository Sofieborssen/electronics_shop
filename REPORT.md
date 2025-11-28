# Electronics Shop - Databasrapport

## Databasdesign

Databasen modellerar en elektronikbutik med tillverkare, produkter, kunder, beställningar och recensioner.

### Tabellstruktur

6 tabeller:

- **brands** - Tillverkare (namn, land, grundat år)
- **products** - Produkter (namn, tillverkare, SKU, pris, kategori, lager)
- **customers** - Kunder (namn, email, telefon, stad)
- **orders** - Beställningar (kund, datum, belopp, status)
- **order_items** - Beställningsrader (beställning, produkt, kvantitet, pris)
- **reviews** - Recensioner (produkt, kund, betyg, kommentar)

### Constraints

- Primary keys: `id` på alla tabeller
- Foreign keys: ON DELETE CASCADE där relevant
- CHECK: price > 0, stock_quantity >= 0, quantity > 0, rating 1-5
- UNIQUE: products.sku, customers.email
- Defaults: status='pending', order_date=CURRENT_DATE, etc.

## Index och optimering

### Identifierade flaskhalsar

**Query 2:** Produkter dyrare än 5000 kr
- Problem: Utan index på price krävs sekventiell skanning
- Lösning: B-tree index på price

**Query 9:** Kunder som har spenderat mest totalt
- Problem: Filtrerar på status='completed' utan index
- Lösning: Partiellt index på completed orders

### Skapade index

1. `idx_products_price` - För prisfiltrering
2. `idx_orders_completed_customer_amount` - Partiellt index för completed orders

**Resultat:** Kostnad minskade med >50% för båda queries.

Ytterligare index i sql/schema.sql: foreign keys, unique constraints, sökindex.

## SQL Queries

**Grundläggande (4):** SELECT, WHERE, ORDER BY

**JOIN (3):** INNER JOIN, multi-JOIN

**Aggregering (3):** GROUP BY, COUNT, SUM, AVG, HAVING

**Avancerade (VG):** Subqueries, window functions (ROW_NUMBER, RANK), CASE

## Python-applikation

SQLAlchemy ORM med:
- `database.py` - Databasanslutning
- `models.py` - ORM-modeller
- `queries.py` - Query-funktioner
- `main.py` - Huvudprogram

9 funktioner implementerade. Parameteriserade queries för säkerhet.

## Sammanfattning

✅ 6 tabeller med constraints och foreign keys  
✅ 10 grundläggande queries + 6 avancerade queries  
✅ 2 index för optimering  
✅ Python-applikation med SQLAlchemy ORM

