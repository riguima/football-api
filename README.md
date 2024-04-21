# football-api

API para Futebol para coletar de dados dos jogos

## Instalação

Segue script para instalação:

```
git clone https://github.com/riguima/football-api
cd football-api
pip install -r requirements.txt
```

Rode com `flask run`

## Rotas

- `/games/<date>/<competition>` - Para mostrar os jogos em uma data e competição específicas.
- `/competitions/<date>` - Para mostrar as competições que ocorreram em uma data específica.
