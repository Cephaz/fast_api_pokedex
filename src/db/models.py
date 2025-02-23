
from src.db.database import Base

from sqlalchemy import JSON, Column, Integer, String

from src.db.database import engine

class Pokemon(Base):
    __tablename__ = "Pokemon"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    types = Column(JSON)
    total = Column(Integer)
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    attack_special = Column(Integer)
    defense_special = Column(Integer)
    speed = Column(Integer)
    evolution_id = Column(Integer, nullable=True)

Base.metadata.create_all(engine)