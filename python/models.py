"""ORM-modeller för Electronics Shop."""

from __future__ import annotations

from datetime import date
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, DECIMAL, Text, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Brand(Base):
    """Brand modell."""

    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    country = Column(String(120))
    founded_year = Column(Integer)
    description = Column(Text)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    products = relationship(
        "Product", back_populates="brand", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Brand(id={self.id}, name='{self.name}')>"


class Product(Base):
    """Product modell."""

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    brand_id = Column(Integer, ForeignKey(
        'brands.id', ondelete='CASCADE'), nullable=False, index=True)
    sku = Column(String(120), unique=True, index=True)
    release_year = Column(Integer)
    price = Column(DECIMAL(10, 2), nullable=False)
    warranty_months = Column(Integer)
    category = Column(String(120), index=True)
    stock_quantity = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    brand = relationship("Brand", back_populates="products")
    order_items = relationship(
        "OrderItem", back_populates="product", cascade="all, delete-orphan")
    reviews = relationship(
        "Review", back_populates="product", cascade="all, delete-orphan")
    __table_args__ = (
        CheckConstraint('price > 0', name='chk_price_positive'),
        CheckConstraint('stock_quantity >= 0',
                        name='chk_stock_quantity_positive'),
    )

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"


class Customer(Base):
    """Customer modell."""

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone = Column(String(60))
    city = Column(String(120), index=True)
    registration_date = Column(Date, default=date.today, index=True)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    orders = relationship("Order", back_populates="customer",
                          cascade="all, delete-orphan")
    reviews = relationship(
        "Review", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.first_name} {self.last_name}', email='{self.email}')>"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Order(Base):
    """Order modell."""

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey(
        'customers.id', ondelete='CASCADE'), nullable=False, index=True)
    order_date = Column(Date, default=date.today, index=True)
    total_amount = Column(DECIMAL(12, 2))
    status = Column(String(50), default='pending', index=True)
    shipping_city = Column(String(120))
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship(
        "OrderItem", back_populates="order", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Order(id={self.id}, customer_id={self.customer_id}, total_amount={self.total_amount}, status='{self.status}')>"


class OrderItem(Base):
    """OrderItem modell."""

    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey(
        'orders.id', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey(
        'products.id', ondelete='CASCADE'), nullable=False, index=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")
    __table_args__ = (
        CheckConstraint('quantity > 0', name='chk_quantity_positive'),
        CheckConstraint('unit_price > 0', name='chk_unit_price_positive'),
    )

    def __repr__(self):
        return f"<OrderItem(id={self.id}, order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity})>"


class Review(Base):
    """Review modell."""

    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey(
        'products.id', ondelete='CASCADE'), nullable=False, index=True)
    customer_id = Column(Integer, ForeignKey(
        'customers.id', ondelete='CASCADE'), nullable=False, index=True)
    rating = Column(Integer, nullable=False)
    comment = Column(Text)
    review_date = Column(Date, default=date.today)
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=False)

    product = relationship("Product", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")
    __table_args__ = (
        CheckConstraint('rating BETWEEN 1 AND 5', name='chk_rating_range'),
    )

    def __repr__(self):
        return f"<Review(id={self.id}, product_id={self.product_id}, customer_id={self.customer_id}, rating={self.rating})>"
