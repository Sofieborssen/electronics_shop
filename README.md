# Electronics Shop

Databassystem för en elektronikbutik. PostgreSQL-databas med Python-applikation som använder SQLAlchemy ORM.

## Projektstruktur

```
electronics_shop/
├── sql/
│   ├── schema.sql              # Databasschema (för psql)
│   ├── schema_pgadmin.sql      # Databasschema (för pgAdmin 4)
│   ├── testdata.sql            # Testdata
│   ├── queries.sql             # SQL-queries (10 st - G-nivå)
│   ├── queries_advanced.sql    # Avancerade queries (6 st - VG-nivå)
│   └── optimization.sql        # Index och optimering (VG-nivå)
├── python/
│   ├── database.py            # Databasanslutning (SQLAlchemy ORM)
│   ├── models.py              # ORM-modeller
│   ├── queries.py             # Query-funktioner
│   ├── main.py                # Huvudprogram
│   └── requirements.txt       # Python-paket
├── README.md                  # Denna fil
└── REPORT.md                  # Dokumentation (VG-nivå)
```

## Krav

- PostgreSQL 14+
- Python 3.10+

## Installation (pgAdmin 4)

### 1. Skapa databasen

I pgAdmin 4:
1. Högerklicka på "Databases" → "Create" → "Database"
2. Namn: `electronics_db`
3. Klicka "Save"

### 2. Skapa tabeller

1. Högerklicka på `electronics_db` → "Query Tool"
2. Öppna filen `sql/schema_pgadmin.sql`
3. Kopiera innehållet och kör (F5 eller Execute)

**Alternativt:** Om du använder psql:
```bash
psql -U <användarnamn> -f sql/schema.sql
```

### 3. Ladda testdata

1. I Query Tool (fortfarande ansluten till `electronics_db`)
2. Öppna filen `sql/testdata.sql`
3. Kopiera innehållet och kör (F5)

**Alternativt:** Om du använder psql:
```bash
psql -U <användarnamn> -d electronics_db -f sql/testdata.sql
```

Innehåll: 3 tillverkare, 12 produkter, 5 kunder, 10 beställningar, 10 order_items, 10 recensioner.

### 4. Installera Python-paket

```bash
pip install -r python/requirements.txt
```

### 5. Sätt miljövariabler

```bash
export ELECTRONICS_DB_HOST=localhost
export ELECTRONICS_DB_PORT=5432
export ELECTRONICS_DB_NAME=electronics_db
export ELECTRONICS_DB_USER=<användarnamn>
export ELECTRONICS_DB_PASSWORD=<lösenord>
```

## Körning

```bash
cd python
python main.py
```

### Testa SQL-queries i pgAdmin 4

1. Öppna Query Tool för `electronics_db`
2. Öppna filen `sql/queries.sql` eller `sql/queries_advanced.sql`
3. Kopiera innehållet och kör (F5)
4. Se resultat i "Data Output"-fliken

**Tips:** Kör en query i taget för bättre översikt.

## Innehåll

**SQL Queries (G-nivå):**
- 10 queries: grundläggande SELECT, JOIN, aggregering

**Avancerade queries (VG-nivå):**
- 6 queries: subqueries, window functions, CASE

**Python-applikation:**
- SQLAlchemy ORM
- Query-funktioner för alla queries
- Demo-program som visar resultat

## Databasstruktur

6 tabeller: brands, products, customers, orders, order_items, reviews

Foreign keys med ON DELETE CASCADE, CHECK constraints, UNIQUE constraints, index för prestanda.

## Optimering

Se `sql/optimization.sql` och `REPORT.md` för index och prestandaanalys.

