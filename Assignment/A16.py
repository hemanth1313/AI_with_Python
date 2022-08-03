#def fibonaci(number):
number = int(input("Entre the Limits"))
a= 0
b=1
if number <= 1:
    print(a)
elif number == 1:
    print("0")
else:
    for i in range (2,number):
        c = a+b
        a= b
        b=c
print(c)    

#error
