

from sqlalchemy import UUID, Column, String
from Employee.schemas.base_shema import Base

class EmployeeDB(Base):
    __tablename__ = 'Employees'

    id = Column(UUID(as_uuid=True), primary_key=True)
    card = Column(String, nullable=False)
    callname = Column(String, nullable=False)
