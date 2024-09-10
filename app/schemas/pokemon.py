from typing import List, Optional
from pydantic import BaseModel, Field

# Pokemon base class
class PokemonBase(BaseModel):
    name: str = Field(...)
    types: List[str] = Field(...)
    total: int = Field(...)
    hp: int = Field(...)
    attack: int = Field(...)
    defense: int = Field(...)
    attack_special: int = Field(...)
    defense_special: int = Field(...)
    speed: int = Field(...)
    evolution_id: Optional[int] = Field(None)

# Pokemon class
class Pokemon(PokemonBase):
    # Example return data
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 6,
                "name": "Charizard",
                "types": ["Fire", "Flying"],
                "total": 534,
                "hp": 78,
                "attack": 84,
                "defense": 78,
                "attack_special": 109,
                "defense_special": 85,
                "speed": 100,
                "evolution_id": 6
            }
        }
