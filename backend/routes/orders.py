"""
Shopping cart routes for adding and retrieving items.
"""

from fastapi import APIRouter
from ..models import Order
from ..database import orders_collection

router=APIRouter(prefix="/orders",tags=["Orders"])

@router.post("/add")
def add_to_cart(order:Order):
    """
    Place a new for a user.
    """
    order_data=order.model_dump() if hasattr(order,"model_dump") else order.dict()
    orders_collection.insert_one(order_data)
    return {"message":"Order added to cart"}
