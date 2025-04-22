def main(n, m, message):
    unread = [0 for x in range(n)]
    for _ in range(m):
        unread[message - 1] = 0
        for i in range(len(unread)):
            if i != message - 1:
                unread[i] += 1
        print(sum(unread))
main(3, 2, 1)