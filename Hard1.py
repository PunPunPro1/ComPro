n = int(input())
L = list(map(int, input().split()))

isError = False
if (n != len(L)):
    isError = True

parts = input()

while (parts != 'END'):
    parts = parts.split()
    op = parts[0]

    if op == "REVERSE":
        a, b = map(int, parts[1:])
        L[a:b+1] = L[a:b+1][::-1]

    elif op == "MERGE":
        a, b = map(int, parts[1:])
        merged = sum(L[a:b+1])
        L[a:b+1] = [merged]

    elif op == "SWAP":
        a, b = map(int, parts[1:])
        L[a], L[b] = L[b], L[a]

    elif op == "SPLIT":
        a, k = map(int, parts[1:])
        value = L[a]
        base = value // k
        remainder = value % k
        parts = [base + 1] * remainder + [base] * (k - remainder)
        L[a:a+1] = parts
    print(L)
    parts = input()

if (isError):
    print("ERROR")
else:
    print(' '.join(map(str, L)))