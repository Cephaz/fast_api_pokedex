from fastapi import FastAPI
from app.models import pokemon
from app.database import engine
from app.routers import pokemon_router

# Create the database tables
pokemon.Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# Include the router
app.include_router(pokemon_router.router)