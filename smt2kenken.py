# import fileinput
# from pprint import pp
import sys

smt = ""
f = open(sys.argv[1], "r")
smt = f.read()
f.close()

# FOR TESTING ONLY
# pp(smt)

spl = smt.split(";; statistics")
smt = spl[0]
stats = spl[1]

# FOR TESTING ONLY
# print(stats)
# print(smt)

smt = list(map(lambda x: "".join(list(map(
                                    lambda x: "".join(x) ,x.strip().replace("(","").replace(")","").replace("V","").split()[1]))) 
                ,smt.split("\n")[1:-1]))

smt = "".join(smt)

print(smt)

stats = list(map(lambda x: x.replace(":","").split(" ")[1:] ,stats.split("\n")[2:-2]))

stats = {sub[0]:sub[1] for sub in stats}

# labeled_stats = {sys.argv[2]:stats}

# print(stats['time-seconds'])
# print(stats['memory-mb'])
# FOR TESTING ONLY
# pp(labeled_stats)

f = open(sys.argv[2], "a")
f.write(str(stats['time-seconds'])+","+str(stats['memory-mb']))
# f.write(str(stats['memory-mb']))
f.write("\n")
f.close()

# FOR ref ONLY
# python3 smt2kenken.py model.smt stats.txt >out.txt
