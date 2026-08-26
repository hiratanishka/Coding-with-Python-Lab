'''
Program : The Multi-Dimensional Packet Scrambler
Purpose : List Manipulation, Slicing, and Multi-Assignment Unpacking
Author  : Tanishka Hira
Date    : 19-08-2026
'''

#---Stage 1: Input Validation and Test Data---
packet = [1,2,3,0,4,5,6,7,8,0]
if packet and len(packet) >= 10:
    print("Validation passed. Processing packet...")
else:
    print("Validation failed: packet is empty or too short.")

#---Stage 2: The “Middle-Out” Swap---
midpoint = len(packet)//2
front_half = packet[:midpoint]
back_half = packet[midpoint:]
scrambled = back_half[::-1] + front_half
print(id(packet) == id(front_half)) #it's false
print("Initial packet: ", packet)
print("After Stage 2(scrambled): ", scrambled)

#---Stage 3: In-Place Correction---
middle_index = len(scrambled)//2
if type(scrambled[middle_index]) is int:
    scrambled.insert(middle_index + 1, "SYNC-BIT")
print("After Sync-Bit insertion: ", scrambled)
while 0 in scrambled:
    scrambled.remove(0)

#---Stage 4: Memory Integrity Check---
print("After zero removal: ", scrambled)
first, *middle, last = scrambled
print(f"Header: {first} Footer: {last} Body length: {len(middle)}")




























    
