import fileinput
from pprint import pp

smt = ""
for line in fileinput.input():
    smt += line

smt = list(map(lambda x: "".join(list(map(
                                    lambda x: "".join(x) ,x.strip().replace("(","").replace(")","").replace("V","").split()[1]))) 
                ,smt.split("\n")[1:-1]))

smt = "".join(smt)

print(smt)
