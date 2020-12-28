data = {}

def find(child, parent):
    global data
    for p in data[child]:
        if p == parent:
            return True
        elif find (p, parent):
            return True
        else:
            continue
    return False



def main():
    n = int(input())
    lines = [input().split(':') for _ in range(n)]

    for line in lines:
        child = line[0].strip()
        if not child in data:
            data[child] = []
        if len(line) > 1:
            for parent in line[1].split():
                parent = parent.strip()
                if parent not in data[child]:
                    data[child].append(parent)
    
    q = int(input())
    queries = [input().split() for _ in range(q)]

    for query in queries:
        if query[0].strip() == query[1].strip() or find(query[1].strip(), query[0].strip()):
            print('Yes')
        else:
            print('No')


main()