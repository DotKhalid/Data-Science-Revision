book = {}

book["ali"] = {
    "name":"ali",
    "age":23,
    "address": "North Nazimabad"
}

book["usama"] = {
    "name":"usama",
    "age":26,
    "address": "Nazimabad"
}


print(book)

import json

s = json.dumps(book)

with open("C://Users//khalid//book.txt", "w") as f:
    f.write(s)