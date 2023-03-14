numbers = set()
mass = [89677183508,89038688453,89011175862,89058477148,89157652796]
with open("numb.txt") as f:
    for line in f:
        numbers.add(int(line))

first = set()
second = set()
third = set()
forth = set()
fifth = set()

for i in numbers:
    first.add(i-mass[0])
    second.add(i-mass[1])
    third.add(i-mass[2])
    forth.add(i - mass[3])
    fifth.add(i - mass[4])

s = first.intersection(second,third,forth,fifth)
s = s.pop()

f = open("unseednumb.txt","w")
for i in numbers:
    f.write(str(i-s)+"\n")
