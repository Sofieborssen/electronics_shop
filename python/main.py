"""Electronics Shop - Huvudprogram"""

from __future__ import annotations

import sys
from database import init_database, get_db_session
from queries import (
    get_all_products,
    get_products_by_brand,
    get_products_above_price,
    get_customer_orders,
    get_orders_by_year,
    get_pending_orders,
    get_products_with_brands,
    get_top_spending_customers,
    get_products_with_ratings
)
from models import Product, Customer, Order


def print_products(products):
    """Skriv ut produkter."""
    if not products:
        print("Inga produkter hittades.")
        return

    print(f"\n{'='*80}")
    print(f"{'ID':<5} {'Namn':<35} {'Kategori':<15} {'Pris':<12} {'Lager'}")
    print(f"{'-'*80}")
    for product in products:
        price = float(product.price) if product.price else 0
        print(f"{product.id:<5} {product.name[:33]:<35} "
              f"{(product.category or 'N/A')[:13]:<15} {price:<12.2f} {product.stock_quantity}")
    print(f"{'='*80}\n")


def print_orders(orders):
    """Skriv ut beställningar."""
    if not orders:
        print("Inga beställningar hittades.")
        return

    print(f"\n{'='*90}")
    print(f"{'ID':<5} {'Kund-ID':<10} {'Datum':<12} {'Belopp':<12} {'Status':<15} {'Leveransstad'}")
    print(f"{'-'*90}")
    for order in orders:
        amount = float(order.total_amount) if order.total_amount else 0
        print(f"{order.id:<5} {order.customer_id:<10} {order.order_date} "
              f"{amount:<12.2f} {order.status[:13]:<15} {order.shipping_city or 'N/A'}")
    print(f"{'='*90}\n")


def demo_all_products():
    """Hämta alla produkter."""
    print("="*80)
    print("Alla produkter")
    print("="*80)

    db = get_db_session()
    try:
        products = get_all_products(db)
        print_products(products)
        print(f"Totalt antal produkter: {len(products)}")
    finally:
        db.close()


def demo_products_by_brand():
    """Produkter från Apple."""
    print("="*80)
    print("Produkter från Apple")
    print("="*80)

    db = get_db_session()
    try:
        products = get_products_by_brand(db, "Apple")
        print_products(products)
        print(f"Antal Apple-produkter: {len(products)}")
    finally:
        db.close()


def demo_products_above_price():
    """Produkter över 5000 kr."""
    print("="*80)
    print("Produkter över 5000 kr")
    print("="*80)

    db = get_db_session()
    try:
        products = get_products_above_price(db, 5000.0)
        print_products(products)
        print(f"Antal produkter över 5000 kr: {len(products)}")
    finally:
        db.close()


def demo_customer_orders():
    """Beställningar för kund ID 1."""
    print("="*80)
    print("Beställningar för kund ID 1")
    print("="*80)

    db = get_db_session()
    try:
        orders = get_customer_orders(db, 1)
        print_orders(orders)
        print(f"Antal beställningar för kund 1: {len(orders)}")
    finally:
        db.close()


def demo_orders_by_year():
    """Beställningar från 2024."""
    print("="*80)
    print("Beställningar från 2024")
    print("="*80)

    db = get_db_session()
    try:
        orders = get_orders_by_year(db, 2024)
        print_orders(orders)
        print(f"Antal beställningar från 2024: {len(orders)}")
    finally:
        db.close()


def demo_pending_orders():
    """Pending beställningar."""
    print("="*80)
    print("Pending beställningar")
    print("="*80)

    db = get_db_session()
    try:
        orders = get_pending_orders(db)
        print_orders(orders)
        print(f"Antal pending beställningar: {len(orders)}")
    finally:
        db.close()


def demo_products_with_brands():
    """Produkter med tillverkare."""
    print("="*80)
    print("Produkter med tillverkares namn")
    print("="*80)

    db = get_db_session()
    try:
        results = get_products_with_brands(db)
        print(f"\n{'='*80}")
        print(f"{'Produkt':<40} {'Tillverkare':<20} {'Pris'}")
        print(f"{'-'*80}")
        for product, brand_name in results:
            price = float(product.price) if product.price else 0
            print(
                f"{product.name[:38]:<40} {brand_name[:18]:<20} {price:.2f} kr")
        print(f"{'='*80}\n")
        print(f"Totalt antal produkter: {len(results)}")
    finally:
        db.close()


def demo_top_customers():
    """Kunder som spenderat mest."""
    print("="*80)
    print("Kunder som har spenderat mest")
    print("="*80)

    db = get_db_session()
    try:
        results = get_top_spending_customers(db, limit=5)
        print(f"\n{'='*80}")
        print(f"{'Kund':<35} {'Totalt spenderat':<20} {'Antal beställningar'}")
        print(f"{'-'*80}")
        for customer, total_spending, order_count in results:
            spending = float(total_spending) if total_spending else 0
            print(
                f"{customer.full_name[:33]:<35} {spending:<20.2f} {order_count}")
        print(f"{'='*80}\n")
    finally:
        db.close()


def demo_products_with_ratings():
    """Produkter med genomsnittligt betyg."""
    print("="*80)
    print("Produkter med genomsnittligt betyg")
    print("="*80)

    db = get_db_session()
    try:
        results = get_products_with_ratings(db)
        print(f"\n{'='*80}")
        print(f"{'Produkt':<40} {'Genomsnittligt betyg':<25} {'Antal recensioner'}")
        print(f"{'-'*80}")
        for product, avg_rating, review_count in results:
            rating = float(avg_rating) if avg_rating else 0
            print(f"{product.name[:38]:<40} {rating:<25.2f} {review_count}")
        print(f"{'='*80}\n")
    finally:
        db.close()


def main():
    """Huvudprogram."""
    print("\n" + "="*80)
    print("    ELECTRONICS SHOP")
    print("="*80)
    
    try:
        init_database()
        print("Databasanslutning etablerad\n")
    except Exception as e:
        print(f"Kunde inte ansluta till databasen: {e}")
        print("\nKontrollera att:")
        print("  - PostgreSQL körs")
        print("  - Databasen 'electronics_db' finns")
        print("  - Miljövariablerna är inställda:")
        print("    ELECTRONICS_DB_USER")
        print("    ELECTRONICS_DB_PASSWORD")
        sys.exit(1)

    # Kör alla demos
    demo_all_products()
    demo_products_by_brand()
    demo_products_above_price()
    demo_orders_by_year()
    demo_pending_orders()
    demo_customer_orders()
    demo_products_with_brands()
    demo_top_customers()
    demo_products_with_ratings()
    
    print("\n" + "="*80)
    print("    KLART")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()
