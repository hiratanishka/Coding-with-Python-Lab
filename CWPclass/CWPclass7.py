
'''
def describe_pet(name: str, species: str) -> str:
    return f'{name} is a {species}'

print(describe_pet(species = "cat", name = "Tom"))
print(describe_pet(name = "Tom", species = "cat")) #same result


def describe_pet(name:str, species: str = "dog") -> str:
    return f'{name} is a {species}'

print(describe_pet('Rex'))
print(describe_pet('Tom', 'cat'))

'''

def add_item_safely(cart):
    #local_copy = cart[:]
    local_cart = cart.copy()
    local_cart.append('books')
    return local_cart

groc = ['pen','pencil']
new_cart = add_item_safely(groc)
print(new_cart)
