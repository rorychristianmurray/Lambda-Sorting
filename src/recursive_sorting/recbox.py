def recurse_factorial(n):
    if n == 0:
        return 1
    return n * recurse_factorial(n-1)


test1 = recurse_factorial(3)

print(test1)


def iter_factorial(n):
    answer = 1
    for i in range(n, 0, -1):
        answer *= i
    return answer


test2 = recurse_factorial(4)

print(test2)
