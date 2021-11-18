#  part 1
for i in range(150):
    print(i)
#  part 2
for i in range(5,150,5):
    print(i)
# part 3
for i in range(1,100):
    if i%10 == 0:
        i = "Coding Dojo"
    elif i%5 == 0:
         i = "Coding"
    print(i)
# part 4
sum = 0
for i in range(1,500000,2):
    sum = sum + i
print(sum)
# part 5
for i in range(2018,0,-4):
    print(i)
# part 6
lowNum = 1
highNum = 100
mult = 4
for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))