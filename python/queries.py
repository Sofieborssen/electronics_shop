"""Query helpers för Electronics Shop."""

from __future__ import annotations

from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_, func, extract
from models import Product, Brand, Customer, Order, OrderItem, Review


def get_all_products(db: Session) -> List[Product]:
    """Hämta alla produkter sorterade efter namn."""
    return db.query(Product).order_by(Product.name).all()


def get_products_by_brand(db: Session, brand_name: str) -> List[Product]:
    """Hämta alla produkter för en specifik tillverkare."""
    return db.query(Product).join(Brand).filter(
        Brand.name.ilike(f"%{brand_name}%")
    ).order_by(Product.name).all()


def get_products_above_price(db: Session, min_price: float = 5000.0) -> List[Product]:
    """Hämta alla produkter som kostar mer än ett visst belopp."""
    return db.query(Product).filter(Product.price > min_price).order_by(Product.price.desc()).all()


def get_customer_orders(db: Session, customer_id: int) -> List[Order]:
    """Hämta alla beställningar för en specifik kund."""
    return db.query(Order).filter(Order.customer_id == customer_id).order_by(Order.order_date.desc()).all()


def get_orders_by_year(db: Session, year: int = 2024) -> List[Order]:
    """Hämta alla beställningar från ett specifikt år."""
    return db.query(Order).filter(
        extract('year', Order.order_date) == year
    ).order_by(Order.order_date.desc()).all()


def get_pending_orders(db: Session) -> List[Order]:
    """Hämta alla pending beställningar."""
    return db.query(Order).filter(Order.status == 'pending').order_by(Order.order_date).all()


def get_products_with_brands(db: Session) -> List[tuple]:
    """Visa alla produkter med deras tillverkares namn."""
    return db.query(Product, Brand.name.label('brand_name')).join(Brand).order_by(
        Brand.name, Product.name
    ).all()


def get_top_spending_customers(db: Session, limit: int = 5) -> List[tuple]:
    """Hitta kunder som har spenderat mest totalt."""
    return db.query(
        Customer,
        func.sum(Order.total_amount).label('total_spending'),
        func.count(Order.id).label('order_count')
    ).join(Order).filter(
        Order.status == 'completed'
    ).group_by(Customer.id).order_by(
        func.sum(Order.total_amount).desc()
    ).limit(limit).all()


def get_products_with_ratings(db: Session) -> List[tuple]:
    """Visa produkter med genomsnittligt betyg från recensioner."""
    return db.query(
        Product,
        func.round(func.avg(Review.rating), 2).label('average_rating'),
        func.count(Review.id).label('review_count')
    ).outerjoin(Review).group_by(Product.id).having(
        func.count(Review.id) > 0
    ).order_by(
        func.avg(Review.rating).desc(),
        func.count(Review.id).desc()
    ).all()
