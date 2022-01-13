print('Hello world')

x = 'Hvordan har du det?'
y = 10
z = 'Bra'
a = x + z
b = True
lis = []

elever = ['Haidas', 'Erik', 'Bendik']
larer = ['Tor', 'Johannes', 'Mats']

while b:
    # print(y)
    y = y + 1
    lis.append(y)
    if y > 100:
        # break
        b = False
lis[5] = 'hest'

elevlarer = []

elevlarer.append(elever)
elevlarer.append(larer)

print(elevlarer)

print(len(lis))


print(lis)



print(type(y))
print(type(x))
print(type(b))
print(type(lis))
print(x)
print(a)


