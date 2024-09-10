from typing import List
from sqlalchemy.orm import Session
from app.models.pokemon import Pokemon as PokemonModel

# PokemonRepository class
class PokemonRepository:
    @staticmethod
    def get_all_pokemons(db: Session) -> List[PokemonModel]:
        return db.query(PokemonModel).all()
