def main(autori):
    final = ''
    for i in range(len(autori)):
        final += autori[i][0]
    print(final)
autori = [
    ("J.", "K. Rowling"),
    ("George", "R. R. Martin"),
    ("J.R.R.", "Tolkien"),
]
main(autori)