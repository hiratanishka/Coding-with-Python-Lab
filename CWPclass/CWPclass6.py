'''def greet(name):
    message = 'Hello, ' + name + '!'
    return message
result = greet('Asha')
print(result)


def add(a: int, b: int) -> int: #can also write it as def add(a,b)
    return a + b

print(add(2,3))
print(add('2','3'))
print(add('2',3)) #type error ata hai


def min_max(numbers: list) -> tuple:
    return min(numbers), max(numbers)

result = min_max([4,9,1,7])
print(result)


def summarize(readings: list) -> tuple:
    total = sum(readings)
    average = total/len(readings)
    return total, average, max(readings)

data = [12.5,13.1,11.8,14.2,15.0]
total,average, peak = summarize(data)

print(f'Total: {total}, Average: {average:.2f}, Peak: {peak}')

'''
def split_name(full_name: str) -> tuple:
    name = full_name.split()
    first_name = name[0]
    last_name = name[-1]
    return "First name: ", first_name, "Last name: ", last_name

full_name = 'Asha Rao'
print(split_name(full_name))











































