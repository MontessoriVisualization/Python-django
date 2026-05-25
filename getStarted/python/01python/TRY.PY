a=[1,2,3,4]
a.append(5)


for x in range(1,11):
    if(x==5):
        continue
    print(f"5 X {x}= {5*x}")
bro="saugat"
length=len(bro)
for x in range(1,length+1):
    print(bro[(length)-1])
    length-=1
orb=''
for x in bro:
    orb=x+orb
print(orb)

string="teerth"
noof1=0

for x in string:
    for y in string:
        if x==y:
            noof1+=1
    if noof1==1:
        print(x)
        break
    else:
        noof1=0

num=5
frm=1
while num>0:
    frm*=num
    num-=1
print(frm)
    

        

print("hello world")

for x in range(1,1100000000000000):
    num=int(input("Enter a number between 1 and 100: "))
    if num<1 or num>100:
        print("Invalid number, please try again.")
    else:
        print(f"You entered: {num}")
        break

while True:
    num=int(input("Enter a number between 1 and 100: "))
    if num<1 or num>100:
        print("Invalid number, please try again.")
    else:
        print(f"You entered: {num}")
        break

list1=[1,2,3,4,5,1]
count=0
for x in list1:
    for y in list1:
        if x==y:
            count+=1
    if count==1:
        count=0
        continue
    else:
        print(x)
        break