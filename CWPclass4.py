'''student = {'name' : 'Tanishka', 'age' : 22, 'city' : 'New Delhi'}

print(student['name'])
print(student['age'])
print("Name:", student['name'],";", "Age:", student['age'])


user_profile = {'name': 'Tanishka', 'age': 22, 'location': 'New Delhi'}
print(user_profile['location'])
print(user_profile)
user_profile['age'] = 23
user_profile['email'] = 'tanishkahira@gmail.com'
print("Updated:",user_profile)
'''

user_profile = {'name': 'Tanishka', 'age': 23}

'''
if 'email' in user_profile:
    print(user_profile['email'])
else:
    print('No email on file.')

email = user_profile.setdefault('email', 'not needed')
print(email)
print(user_profile)
name = user_profile.setdefault('name', 'Kyu?')
print(name)
print(user_profile)
'''
'''
words = ['ai', 'ml', 'ai', 'nlp', 'ml', 'ai']
counts= {}
for w in words:
    counts[w] = counts.setdefault(w,0)+1
counts['ai'] = counts.setdefault('ai',0)+1
print(counts)
'''

book = {'title': 'Python 101', 'pages': 320}
if 'author' in book:
    print('author is there')
else:
    print('No author mentioned')

book.setdefault('author', 'Unknown')
book['pages']=350
book['edition']=1
print(book)
