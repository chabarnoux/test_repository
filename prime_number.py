number=int(input("Choose the number that you're looking for it's divisors:"))
for i in range(number) :
    if i!=0:
        if number%i==0:
            print(i)