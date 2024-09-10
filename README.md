## init env dependencies
`python3 -m venv .venv`
`pip3 install -r requirements.txt`

## init seed
```
cd seeds
python3 seed_pokemon.py
```

## run server
`uvicorn app.main:app --reload`
