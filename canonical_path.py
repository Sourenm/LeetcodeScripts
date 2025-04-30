def canonical_path(s):
    folders = s.split("/")
    canonical = []
    for i in range(len(folders)):
        if (i > 0 and folders[i] == '.') or folders[i].find('/') != -1 or folders[i] == '':
            continue
        elif folders[i] == '..' and i > 0:
            canonical = canonical[:-1]
        else:
            canonical.append(folders[i])
    return "/" + "/".join(canonical)

path = '/home/user/Documents/../Pictures'
print(canonical_path(path))
