n =int(input())
if (n>0 and n<10):
    print("satuan")
elif(n<100):
    print("puluhan")
elif(n<1000):
    print("ratusan")
elif(n<10000):
    print("ribuan")
elif(n<100000):
    print("puluhribuan")
else:
    exit()