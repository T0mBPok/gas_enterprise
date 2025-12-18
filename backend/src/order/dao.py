from src.dao.base import BaseDAO
from src.order.models import Order
from src.customer.dao import CustomerDAO
from src.delivery.dao import DeliveryDAO


class OrderDAO(BaseDAO):
    model = Order

    @classmethod
    async def get_one_with_relations(cls, id: int):
        order = await cls.get_one_by_id(id, "status")

        if order:
            # deliveries = await DeliveryDAO.get_all_with_relations(order_id=order.id)
            # order.deliveries = deliveries

            if order.customer_id:
                customer = await CustomerDAO.get_one_by_id(
                    order.customer_id, "country", "city", "street", "house"
                )
                order.customer = customer

        return order

    @classmethod
    async def get_all_with_relations(cls, **filter_by):
        orders = await cls.get_all("status", **filter_by)

        for o in orders:
            # deliveries = await DeliveryDAO.get_all_with_relations(order_id=o.id)
            # o.deliveries = deliveries

            if o.customer_id:
                customer = await CustomerDAO.get_one_by_id(
                    o.customer_id, "country", "city", "street", "house"
                )
                o.customer = customer

        return orders