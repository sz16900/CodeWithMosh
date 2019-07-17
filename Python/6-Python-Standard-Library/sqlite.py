import sqlite3
import simplejson as json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
print(movies)

# if this doesn't exists, this method will create it for us
with sqlite3.connect("db.sqlite3") as conn:
