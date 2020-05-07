# if elif else
'''
marks = 88
if marks > 80:
    print("Grade A")
elif (marks > 60)and (marks <= 75):
    print("Grade B")
elif(marks > 40) and (marks <= 60):
    print("Grade C")
else:
    print("Grade D")
    '''

# while
'''
num=int(input('enter the value :'))

if num <= 0:
    print("entered value is less than or eq to zer0o")
else:
    sum = 0
    while(num>0):
        sum+=num
        num-=1

print(sum)
'''
# for Loop
'''
for qty in range(99,0,-1):
    if qty > 1:
        print(qty,"Bottle of beer on the wall",qty,"Bottles of beer")
        if qty > 2:
            suf = str(qty) + "bottles of beer on the wall"
        else:
            suf = "1 bottle of beer on the wall"
    elif qty == 1:
        print("1 bottle of ber on the wall, 1 bottle of beer")

    print("Take one downa and pass it around",suf)
    print("----")
'''

#Break
'''
num=0
while True:
    print(num)
    num+=1
    if num > 10:
        break
'''


#Continue

for i in range(20):
    if(i%2==0):
        continue
    print(i)
