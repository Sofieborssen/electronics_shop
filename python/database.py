"""Database connection utilities."""

from __future__ import annotations

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

Base = declarative_base()
SessionLocal = None


def get_database_url() -> str:
    """Hämta databas-URL från miljövariabler."""
    host = os.getenv('ELECTRONICS_DB_HOST', 'localhost')
    port = os.getenv('ELECTRONICS_DB_PORT', '5432')
    dbname = os.getenv('ELECTRONICS_DB_NAME', 'electronics_db')
    user = os.getenv('ELECTRONICS_DB_USER')
    password = os.getenv('ELECTRONICS_DB_PASSWORD')

    if not user or not password:
        raise KeyError(
            "Saknar miljövariabler: ELECTRONICS_DB_USER och/eller ELECTRONICS_DB_PASSWORD")

    return f"postgresql://{user}:{password}@{host}:{port}/{dbname}"


def init_database():
    """Initiera databasanslutning och skapa session factory."""
    global SessionLocal

    database_url = get_database_url()
    engine = create_engine(
        database_url,
        poolclass=NullPool,
        echo=False
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return engine


def get_db_session():
    """Hämta en databassession."""
    if SessionLocal is None:
        init_database()

    return SessionLocal()
