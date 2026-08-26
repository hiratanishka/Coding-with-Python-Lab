
#while loop w correct indentation and w/o correct indentation
'''count = 1
while count <= 5:
    print(count)
    count += 1
print('Done!')

count = 1
while count <= 5:
    print(count)
count += 1
print('Done!')
'''

#for loop
'''
cats = ['Tom', 'Whiskers', 'Luna']
for cat in cats:
    print(cat, 'says meow')

for letter in 'AI':
    print(letter)

while cat in cats:
    print(cat)
'''

#pitfall: the loop else
'''
for num in [2,4,6,8]:
    if num % 2 != 0:
        break
else:
    print('All numbers were even.')
'''


numbers = [4,9,15,22,7,3,18]
for i in numbers:
    if i %3 == 0:
        print(i)
    
