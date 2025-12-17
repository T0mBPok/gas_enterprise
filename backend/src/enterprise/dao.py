from src.dao.base import BaseDAO
from src.enterprise.models import Enterprise


class EnterpriseDAO(BaseDAO):
    model = Enterprise