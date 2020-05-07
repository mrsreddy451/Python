#Arithemetic Operator
num1 = 10
num2 = 30
'''
print("num1 + num2:", num1 + num2)
print("num1 - num2: ", num1 - num2 )
print("num1 * num2: ", num1 * num2 )
print("num1 / num2:  ", num1 / num2 )
print("num1 ** num2:  ", num1 ** num2 )
print("num1 % num2:  ", num1 % num2 )
print("22//7",28//7)
'''
#Assigning Operator
num3 = num1 + num2

#print('num3',num3)
num3+=num2
#print('num3',num3)

#Comparision Operator
'''
print("is num3 > num2",num3 > num2)
print("is num2 = num1",num2 == num1)
print("num1 != num2" , num1 != num2)
'''

#Logiacal OPerators
'''
x=True
y=False

print('x and y', x and y)
print('x or y', x or y)
print('not y',not y)
'''
#Bitwise OPerator

num4 = 6 #110
num5 = 2 #010
'''
print('Bitwise and=', num4 & num5)
print('Bitwise or =', num4 | num5)
print('Bitwise xor =', num4 ^ num5)
print('num4 right shifted by 2', num4 >> 2)
print('num5 left shifted by 2', num5 << 2)
'''
#Indentity Operators

print('is num4 is 6',num4 is 6)
print('is num5 is not 2',num5 is not 2)

#Membership Operator

num6 = [1,3,4,5,6,6]
print("check 3 in num7",3 in num6)
print("check 3 in num7",3 not in num6)