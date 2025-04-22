def main(db, query):
    sep_query = set(query.split())
    count = -1
    final = []
    for i in range(len(db)):
        temp = set(db[i].split())
        q = temp.intersection(sep_query)
        if len(q) > count:
            count = len(q)
            final = db[i]
    print(final)
database = [
    "apple banana cherry",
    "banana cherry date",
    "apple banana cherry date",
    "banana cherry",
    "apple date"
]
search_query = "apple cherry"
main(database, search_query)