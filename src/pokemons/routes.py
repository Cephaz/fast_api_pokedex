from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.db.models import Pokemon
from src.pokemons.schemas import PokemonResponse
from src.pokemons.service import PokemonService


pokemon_router = APIRouter()
pokemon_service = PokemonService()

@pokemon_router.get("/pokemons", response_model=List[PokemonResponse])
def get_all_pokemons(db: Session = Depends(get_db)):
    return pokemon_service.get_all_pokemons(db)
