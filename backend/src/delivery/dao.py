from src.dao.base import BaseDAO
from src.delivery.models import Delivery


class DeliveryDAO(BaseDAO):
    model = Delivery