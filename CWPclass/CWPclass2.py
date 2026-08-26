str = 'tanishka'
print(str[1:4])
print(str[1:])
print(str[:9])
print(str[-3:-1])
print(str[0:len(str)])


letters = ['a', 'b', 'c', 'd', 'e']
print(letters[1:3])
print(len(letters[1:3]))


nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[0:10:2])
print(nums[1:8:3])
print(nums[::-1])

data = [5,10,15,20,25,30,35,40]
data_1=data[:]
print(data[:3])
print(data[5:len(data)])
print(data[::3])
print(data[::-1])
print(data_1)
print(data.insert(1,2))


sensor_data = [22.5, 'ERROR', 23.0, 21.8, 'ERROR', 24.5]
print(sensor_data)
print('ERROR' in sensor_data)
sensor_data.remove('ERROR')
print(sensor_data)
sensor_data.pop()
print(sensor_data)
