
from dataclasses import field

from attr import dataclass


@dataclass(frozen=True)
class TransaccionDTO(DTO):
    valor = str = field(default_factory=str)
    fecha = db.Column(db.DateTime, nullable=False)
    divisa_id = db.Column(db.String, db.ForeignKey("divisa.id"))
