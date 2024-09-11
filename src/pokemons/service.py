from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.db.models import Pokemon

class PokemonService:
    def get_all_pokemons(self, db: Session):
        return db.query(Pokemon).all()
