from sqlalchemy.orm import Session

from src.db.models import Pokemon

class PokemonService:
    def get_all_pokemons(self, db: Session):
        return db.query(Pokemon).order_by(Pokemon.id)
