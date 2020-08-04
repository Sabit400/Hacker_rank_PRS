n = int(input())

if n % 2 != 0:
    print(n,"Weird")
else:
    if n >=2 and n <= 5:
        print(n,"Not Weird")
    elif n >= 6 and n <= 20:
        print (n,"Weird")
    else:
        print(n,"Not Weird")