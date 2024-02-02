def is_power_of_two(n):
    if n <= 0:
        return "bukan"
    return "ya" if (n & (n - 1)) == 0 else "bukan"

n = int(input())
result = is_power_of_two(n)
print(result)


