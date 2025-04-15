#using zip
#using zip to iterate over two lists

ids = [101, 102, 103, 104]
names = ['John', 'Jane', 'Jim', 'Jack']

for id, name in zip(ids, names):
    print(f"The ID", id, "is assigned to", name)