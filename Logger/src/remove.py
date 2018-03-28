import re

made = re.compile("\s*@created\([0-9]*T[0-9]*\)")
fin = re.compile("\s*@done\([0-9]*T[0-9]*\)")

path = "other.txt"

file = open(path,'r')

for line in file:
    if made.search(line):
        re.sub(made,"",line)
    elif fin.search(line):
        re.sub(fin,"",line)
    else:
        print(line)

file.close()