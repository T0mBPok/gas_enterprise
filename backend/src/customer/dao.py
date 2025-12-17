from src.dao.base import BaseDAO
from src.customer.models import Customer


class CustomerDAO(BaseDAO):
    model = Customer