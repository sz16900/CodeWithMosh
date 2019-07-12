import simplejson as json

movies = [
    {"id": 1, "title": "terminator", "year": 1998},
    {"id": 2, "title": "toystory", "year": 1999}
]

data = json.dumps(movies)
print(data)
