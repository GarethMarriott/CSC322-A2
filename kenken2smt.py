import fileinput
from pprint import pp

# (set-logic UFNIA)
# (set-option :produce-models true)
# (set-option :produce-assignments true)
# (declare-const V0 Int)
# (declare-const V1 Int)
# (declare-const V2 Int)

smt = ""
smt += "(set-logic UFNIA)\n"
smt += "(set-option :produce-models true)\n"
smt += "(set-option :produce-assignments true)\n"

for i in range(0,81):
    smt += f"(declare-const V{i} Int)\n"

for i in range(0,81):
    smt += f"(assert (and (> V{i} 0) (< V{i} 10)))\n"

for i in range(0,9):
    j = i*9
    smt += f"(assert (distinct V{j} V{j+1} V{j+2} V{j+3} V{j+4} V{j+5} V{j+6} V{j+7} V{j+8} ))\n"

for i in range(0,9):
    smt += f"(assert (distinct V{i} V{i+9} V{i+18} V{i+27} V{i+36} V{i+45} V{i+54} V{i+63} V{i+72} ))\n"

kenken = ""
for line in fileinput.input():
    kenken += line

pp(kenken)


smt += "(check-sat)\n"
smt += "(get-value (V0 V1 V2 V3 V4 V5 V6 V7 V8 V9 V10 V11 V12 V13 V14 V15 V16 V17 V18 V19 V20 V21 V22 V23 V24 V25 V26 V27 V28 V29 V30 V31 V32 V33 V34 V35 V36 V37 V38 V39 V40 V41 V42 V43 V44 V45 V46 V47 V48 V49 V50 V51 V52 V53 V54 V55 V56 V57 V58 V59 V60 V61 V62 V63 V64 V65 V66 V67 V68 V69 V70 V71 V72 V73 V74 V75 V76 V77 V78 V79 V80 ))\n"
smt += "(exit)\n"
print(smt)