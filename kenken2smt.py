import fileinput
from pprint import pp

kenken = ""
for line in fileinput.input():
    kenken += line

pp(kenken)

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

