def main(n, path):
    cost = path[0] + path[1]
    ind = []
    ind.append(0)
    ind.append(1)
    visited = [0 for x in range(n)]
    visited[0] = 1
    visited[1] = 1
    current = 1
    next = 2
    while current != (n - 1):
        sum = next
        temp = next + 1
        while sum < (n - 1 - current):
            sum += temp
            temp += 1
        if sum == (n - 1 - current):
            while current != (n - 1):
                current += next
                ind.append(current)
                next += 1
                if visited[current] != 1:
                    cost += path[current]
            break
        elif sum == (n - current):
            current -= 1
            ind.append(current)
            if visited[current] != 1:
                cost += path[current]
            while current != (n - 1):
                current += next
                ind.append(current)
                next += 1
                if visited[current] != 1:
                    cost += path[current]
            break
        else:
            if (current + next) > (n - 1):
                current -= 1
                ind.append(current)
                if visited[current] != 1:
                    cost += path[current]
            elif visited[current - 1] == 0 and visited[current + next] == 0:
                if path[current - 1] < path[current + next]:
                    current -= 1
                    ind.append(current)
                    if visited[current] != 1:
                        cost += path[current]
                else:
                    current += next
                    ind.append(current)
                    next += 1
                    if visited[current] != 1:
                        cost += path[current]
            elif visited[current - 1] == 1:
                current -= 1
                ind.append(current)
                if visited[current] != 1:
                    cost += path[current]
            else:
                current += next
                ind.append(current)
                next += 1
                if visited[current] != 1:
                    cost += path[current]
    print(cost)
    print(ind)
main(8, [3, 2, 5, 4, 1, 2, 3, 6])
