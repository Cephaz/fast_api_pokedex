# seeds/seed_pokemon.py

import json
import asyncio
import aiosqlite

async def create_tables(db):
    await db.execute('''
    CREATE TABLE IF NOT EXISTS Pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        types TEXT NOT NULL,
        total INTEGER,
        hp INTEGER,
        attack INTEGER,
        defense INTEGER,
        attack_special INTEGER,
        defense_special INTEGER,
        speed INTEGER,
        evolution_id INTEGER
    )
    ''')
    await db.commit()

async def insert_pokemon(db, pokemon):
    await db.execute('''
    INSERT INTO Pokemon (id, name, types, total, hp, attack, defense, attack_special, defense_special, speed, evolution_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        pokemon['id'],
        pokemon['name'],
        json.dumps(pokemon['types']),
        pokemon['total'],
        pokemon['hp'],
        pokemon['attack'],
        pokemon['defense'],
        pokemon['attack_special'],
        pokemon['defense_special'],
        pokemon['speed'],
        pokemon.get('evolution_id')
    ))

async def seed_database():
    # Charger les données JSON
    with open('./pokemons.json', 'r') as file:
        pokemon_data = json.load(file)

    # Connexion à la base de données SQLite
    async with aiosqlite.connect('pokemon.db') as db:
        await create_tables(db)
        
        # Insérer les données
        for pokemon in pokemon_data:
            await insert_pokemon(db, pokemon)
        
        await db.commit()

    print("Seeding terminé avec succès!")

# Exécuter le script de seeding
if __name__ == "__main__":
    asyncio.run(seed_database())