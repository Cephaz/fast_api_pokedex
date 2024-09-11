from typing import List

from fastapi import APIRouter, Depends
from fastapi_pagination import Page, Params
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.pokemons.schemas import PokemonResponse
from src.pokemons.service import PokemonService
from fastapi_pagination.ext.sqlalchemy import paginate


pokemon_router = APIRouter()
pokemon_service = PokemonService()

@pokemon_router.get("/pokemons", response_model=Page[PokemonResponse])
def get_all_pokemons(db: Session = Depends(get_db)):
    return paginate(pokemon_service.get_all_pokemons(db))
