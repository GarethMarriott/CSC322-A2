import fileinput
from pprint import pp
import sys

smt = ""
for line in fileinput.input():
    smt += line

smt = list(map(lambda x: "".join(list(map(
                                    lambda x: "".join(x) ,x.strip().replace("(","").replace(")","").replace("V","").split()[1]))) 
                ,smt.split("\n")[1:-1]))

smt = "".join(smt)

print(smt)

f = open(sys.argv[0], "a")
f.write("Now the file has more content!")
f.close()
