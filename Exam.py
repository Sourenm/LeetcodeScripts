def main(n):
    final = ''
    i = 0
    while i < len(n):
        final += n[i]
        if n[i] == 'a' or n[i] == 'i' or n[i] == 'o' or n[i] == 'u' or n[i] == 'e':
            for j in range(i + 1, len(n)):
                if n[j] != n[i]:
                    break
                else:
                    i += 1
        i += 1
    print(final)

main("Hello")