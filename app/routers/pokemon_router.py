from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.pokemon_repository import PokemonRepository
from app.schemas.pokemon import Pokemon

# pokemon router
router = APIRouter()

@router.get("/pokemons", response_model=List[Pokemon])
def get_all_pokemons(db: Session = Depends(get_db)):
    return PokemonRepository.get_all_pokemons(db)