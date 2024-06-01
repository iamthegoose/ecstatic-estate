from app.services.models.base import Base
from sqlalchemy.orm import Mapped, mapped_column
from app.services.types.schema import Roles


class Flat(Base):
    __tablename__ = "flats"
    id: Mapped[int] = mapped_column(
        primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(index=True, nullable=False)
    location: Mapped[str] = mapped_column(index=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    area: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    rooms: Mapped[int] = mapped_column(nullable=False)
    