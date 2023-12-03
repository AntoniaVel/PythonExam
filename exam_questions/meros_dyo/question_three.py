def divisors(n):
    # dummy implemenation of divisors
    if n == 90:
        return [1, 2, 3, 5, 6, 9, 10, 15, 18, 30, 45, 90]
    elif n == 30:
        return [1, 2, 3, 5, 6, 10, 15, 30]
    elif n == 60:
        return [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]


def gcd(numbers):
    # Solution with set and intersection
    div = [divisors(i) for i in numbers]
    commonDivisors = set(div[0]).intersection(*div)
    return max(commonDivisors)


def gcd2(numbers):
    # Solution with list enumeration
    div = [divisors(i) for i in numbers]
    commonDivisors = set()
    for i, row in enumerate(div):  # div columns
        for j in range(len(row)):  # div rows
            element = row[j]
            if (all(element in other_row for other_row in div if other_row != row) and element not in commonDivisors):
                commonDivisors.add(element)
    return max(commonDivisors)


print(gcd([30, 90, 60]))
print(gcd2([30, 90, 60]))
