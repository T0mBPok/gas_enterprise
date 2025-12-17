from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey
from src.database import Base
from src.enterprise.models import Enterprise
from src.well.models import Well
from src.classifiers.models import ProcessType, ProcessStatus

class ProductionProcess(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    date_start: Mapped[date | None]
    date_end: Mapped[date | None]
    notes: Mapped[str | None]

    enterprise_id: Mapped[int] = mapped_column(ForeignKey("enterprises.id"))
    well_id: Mapped[int | None] = mapped_column(ForeignKey("wells.id"))
    type_id: Mapped[int] = mapped_column(ForeignKey("processtypes.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("processstatuses.id"))
    
    enterprise: Mapped["Enterprise"] = relationship("Enterprise")
    well: Mapped["Well"] = relationship("Well")
    status: Mapped["ProcessStatus"] = relationship("ProcessStatus")
    type: Mapped['ProcessType'] = relationship("ProcessType")