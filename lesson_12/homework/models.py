"""
# 1:
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
# 2:
Создать таблицу покупок. Атрибуты: id, ссылка на пользователя, ссылка на продукт, количество.
"""

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    purchases = relationship("Purchase", back_populates="user")


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    amount = Column(Integer)
    comment = Column(String)

    purchases = relationship("Purchase", back_populates="product")


class Purchase(Base):
    __tablename__ = "purchase"
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"), primary_key=True)
    product_id = Column(ForeignKey("product.id"), primary_key=True)
    amount = Column(Integer)

    user = relationship("User", back_populates="purchases")
    product = relationship("Product", back_populates="purchases")
