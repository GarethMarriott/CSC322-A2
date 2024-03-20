import fileinput
from pprint import pp
import re
import itertools

def split_num_op(s):
    r = re.compile("([\d]+)([\D]+)?")
    m = r.match(s)
    return (m.group(1),m.group(2))

def get_nex_plus(ls):
    if len(ls) == 1:
        return f"V{ls[0]}"
    else:
        return f"(+ V{ls[0]} {get_nex_plus(ls[1:])})"

def get_nex_mult(ls):
    if len(ls) == 1:
        return f"V{ls[0]}"
    else:
        return f"(* V{ls[0]} {get_nex_mult(ls[1:])})"


smt = ""
smt += "(set-logic UFNIA)\n"
smt += "(set-option :produce-models true)\n"
smt += "(set-option :produce-assignments true)\n"

for i in range(0,49):
    smt += f"(declare-const V{i} Int)\n"

for i in range(0,49):
    smt += f"(assert (and (> V{i} 0) (< V{i} 8)))\n"

for i in range(0,7):
    j = i*7
    smt += f"(assert (distinct V{j} V{j+1} V{j+2} V{j+3} V{j+4} V{j+5} V{j+6} ))\n"

for i in range(0,7):
    smt += f"(assert (distinct V{i} V{i+7} V{i+14} V{i+21} V{i+28} V{i+35} V{i+42} ))\n"

kenken = ""
for line in fileinput.input():
    kenken += line

# pp(kenken)

raw_conditions = kenken.split("\n")
# pp(raw_conditions)
conditions = []
for line in raw_conditions:
    if line == "" or line[0] == "#":
        pass
    else:
        conds = line.split(",")
        conditions += conds
# pp(len(conditions))
# pp(conditions)

conds_dict = {}
for i,cond in enumerate(conditions):
    c = cond.split(".")
    if len(c) >= 2:
        # pp(c)
        num,op = split_num_op(c[1])
        if op == None:
            op = "="
        conds_dict[(c[0],num,op)] = [i]
    else:
        for key in conds_dict.keys():
            if key[0] == cond:
                conds_dict[key].append(i)
    # pp(conds_dict)

# pp(conds_dict)


        
for key,val in conds_dict.items():
    cond_str = f"(assert "
    match key[2]:
        case "=":
            cond_str += f"(= {key[1]} V{val[0]}))\n"
        case "-":
            cond_str += f"(or (= {key[1]} (- V{val[0]} V{val[1]})) (= {key[1]} (- V{val[1]} V{val[0]}))))\n"
        case "/":
            cond_str += f"(or (= {key[1]} (/ V{val[0]} V{val[1]})) (= {key[1]} (/ V{val[1]} V{val[0]}))))\n"
        case "+":
            cond_str += f"(= {key[1]} "
            cond_str += f"{get_nex_plus(val)}))\n"
    smt += cond_str
    
smt += "(check-sat)\n"
smt += "(get-value (V0 V1 V2 V3 V4 V5 V6 V7 V8 V9 V10 V11 V12 V13 V14 V15 V16 V17 V18 V19 V20 V21 V22 V23 V24 V25 V26 V27 V28 V29 V30 V31 V32 V33 V34 V35 V36 V37 V38 V39 V40 V41 V42 V43 V44 V45 V46 V47 V48))\n"
smt += "(exit)\n"
print(smt)