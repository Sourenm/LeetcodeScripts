def main(n, t, collection):
    if n == 1:
        print('""')
    else:
        length = 1
        song = 0
        current = collection[song]
        result = []
        ind = 0
        while current != len(collection) - 1:
            query = current[ind: ind + length]
            while query == ' ' or query == '-':
                ind += 1
                query = current[ind: ind + length]
            flag = 0
            for i in range(0, len(collection)):
                if collection[i] != current:
                    if query in collection[i]:
                        flag = 1
                        break
            if flag == 0:
                result.append(query)
                if song + 1 >= len(collection):
                    break
                else:
                    song += 1
                    current = collection[song]
                    ind = 0
                    length = 1
            else:
                if ind + length > len(collection[0]) - 1:
                    if ind == 0:
                        result.append(':(')
                        if song + 1 >= len(collection):
                            break
                        else:
                            song += 1
                            current = collection[song]
                            ind = 0
                            length = 1
                    else:
                        length += 1
                        ind = 0
                else:
                    ind += 1
        print(result)

n = 4
t = 3
collection = [
    "the quick brown fox",
    "jumps over the lazy dog",
    "hello world",
    "programming is fun"
]
main(n, t, collection)
