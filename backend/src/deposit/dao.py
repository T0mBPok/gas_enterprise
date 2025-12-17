from src.dao.base import BaseDAO
from src.deposit.models import Deposit


class DepositDAO(BaseDAO):
    model = Deposit