total =0
while True:
    try:
        n = input()
        
        if not n:
            break
        total += int(n)
    except EOFError:
        break
print(total)