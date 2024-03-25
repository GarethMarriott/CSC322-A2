# import fileinput
# from pprint import pp
import sys

def print_puzzle(puzzle_str):
    size = int(len(puzzle_str) ** 0.5)
    for i in range(size):
        for j in range(size):
            print(puzzle_str[i*size + j], end=' ')
        print()

smt = ""
f = open(sys.argv[1], "r")
smt = f.read()
f.close()

pretty_print = False
if len(sys.argv) > 3 and sys.argv[3] == "--pretty":
    pretty_print = True

spl = smt.split(";; statistics")
smt = spl[0]
stats = spl[1]

smt = list(map(lambda x: "".join(list(map(
                                    lambda x: "".join(x) ,x.strip().replace("(","").replace(")","").replace("V","").split()[1]))) 
                ,smt.split("\n")[1:-1]))

smt = "".join(smt)

if pretty_print:
    print("KenKen Puzzle:")
    print_puzzle(smt)
else:
    print(smt)

stats = list(map(lambda x: x.replace(":","").split(" ")[1:] ,stats.split("\n")[2:-2]))

stats = {sub[0]:sub[1] for sub in stats}

f = open(sys.argv[2], "a")
f.write(str(stats['time-seconds'])+","+str(stats['memory-mb']))
f.write("\n")
f.close()