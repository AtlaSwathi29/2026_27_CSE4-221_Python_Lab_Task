#10:35
a = int(input("Enter first numb: "))
b = int(input("Enter second numb: "))
c = int(input("Enter third numb: "))

if  a <= b: 

    if a<= c: 
        smallest = a
    else:
        smallest = c
else:
    if b <= c: 
        smallest =  b
    else:
        smallest = c

print(f"Smallest = {smallest} (among {a}, {b}, {c})")