keys = input().split()
values = input().split()
myzip = zip(keys, map(float, values))
print(dict(myzip))