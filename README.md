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

- `/jogos/<date>/<competition>` - Para mostrar os jogos de uma data e competição específicas.
- `/jogos/hoje/<competition>` - Para mostrar os jogos de hoje de competição específicas.
- `/jogos/ontem/<competition>` - Para mostrar os jogos de ontem de competição específicas.
- `/jogos/amanha/<competition>` - Para mostrar os jogos de amanhã de competição específicas.
- `/jogos/<date>` - Para mostrar os jogos de todas as competições de uma data específica.
- `/jogos/hoje` - Para mostrar os jogos de todas as competições de hoje.
- `/jogos/ontem` - Para mostrar os jogos de todas as competições de ontem.
- `/jogos/amanha` - Para mostrar os jogos de todas as competições de amanhã.
- `/competicoes/<date>` - Para mostrar as competições que ocorreram de uma data específica.
- `/competicoes/hoje` - Para mostrar as competições que ocorreram e ocorrerão hoje.
- `/competicoes/ontem` - Para mostrar as competições que ocorreram ontem.
- `/competicoes/amanha` - Para mostrar as competições que ocorrerão amanhã.
