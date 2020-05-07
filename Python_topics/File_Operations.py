'''
fp = open("D:\Raja.txt",'w+')
fp.write("Raja Sekhar Reddy M")
fp.seek(0)
print(fp.read())
fp.close()

#print(fp.read())
'''
Money =300
def addmo():
    #global Money
    Money=100
    Money = Money +1000
    print(Money)

print(Money)
addmo()
print(Money)