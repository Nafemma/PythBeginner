#for loops
#<----------------Example1---------------->
'''for i in range(1,5): #stops at 4
    print(i)
print("Final value of i:", i)'''

#<----------------Example2---------------->
'''names = ["Mulungu Alinafe", "Isabelle", "Elizabeth", "Tinashe"]
for name in names:
    print(name)'''

#<----------------Example3---------------->
#using enumerate to get index and value
'''surnames = ['Mpofu', 'Banda', 'Kamphinda']

for index, surname in enumerate(surnames):
    print(index, surname)'''

#<----------------Example4---------------->
#multiplication table

multiplier = 5

for i in range(1, 13):
    print(f"{i} X {multiplier} = {i * multiplier}")