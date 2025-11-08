
"""
while True:
    print("1")

i=0
while i<10:
    print(i)
    i+=1

for i in range(10):
    print(i)

sum=0
for i in range(10):
    sum+=i
print(sum)


num=684563
count=0
while num != 0:
    num=num//10
    count+=1
print(count)
"""
count = 8
num1=0
num2=1
print(num1)
print(num2)
for i in range(count):
    temp=num1+num2
    num1=num2
    num2=temp
    print(num2)