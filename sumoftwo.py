n = int(input())
arr = [0]*n

for i in range(n):
    arr[i] = int(input())

target = int(input())

for x in range(n):
    for y in range(1, n):
        if (arr[x] + arr[y] == target):
            print(f"{x},{y}")
            break