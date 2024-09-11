from typing import List, Optional
from pydantic import BaseModel, Field


class PokemonBase(BaseModel):
    id: int
    name: str
    types: List[str]
    total: int
    hp: int
    attack: int
    defense: int
    attack_special: int
    defense_special: int
    speed: int
    evolution_id: Optional[int] = Field(None)

class PokemonResponse(PokemonBase):
    id: int
    
    class Config:
        from_attributes = True
