from src.dao.base import BaseDAO
from src.delivery.models import Delivery
from src.enterprise.dao import EnterpriseDAO


class DeliveryDAO(BaseDAO):
    model = Delivery

    @classmethod
    async def get_one_with_relations(cls, id: int):
        delivery = await cls.get_one_by_id(id, "status", "transport")

        if delivery:
            if delivery.enterprise_id:
                enterprise = await EnterpriseDAO.get_one_with_deposit(delivery.enterprise_id)
                delivery.enterprise = enterprise

            if delivery.order_id:
                from src.order.dao import OrderDAO
                order = await OrderDAO.get_order_by_id(delivery.order_id)
                delivery.order = order

        return delivery

    @classmethod
    async def get_all_with_relations(cls, **filter_by):
        deliveries = await cls.get_all("status", "transport", **filter_by)

        for d in deliveries:
            if d.enterprise_id:
                enterprise = await EnterpriseDAO.get_one_with_deposit(d.enterprise_id)
                d.enterprise = enterprise

            if d.order_id:
                from src.order.logic import OrderLogic
                order = await OrderLogic.get_order_by_id(d.order_id)
                d.order = order

        return deliveries