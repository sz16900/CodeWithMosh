import simplejson as json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "terminator", "year": 1998},
#     {"id": 2, "title": "toystory", "year": 1999}
# ]

# data = json.dumps(movies)
# print(data)


# then...

data = Path("movies.json",).read_text()
movies = json.loads(data)
print(movies)
