'''num = int(input("num:"))
i = 2
prime = True
while i < num:
    if (num%i == 0):
        print("not prime")
        prime = False
        break
    i = i+1
    if prime:
        print("prime")
        break'''

prime = True
i = 2
for i in range(2,10):
    if i%2 == 0:
        prime = False
    i = i+1
    if prime:
        print (i)
    



        
