# import fileinput
# from pprint import pp
# import json
import pandas as pd
import xlsxwriter
import sys

# stats = ""
f = open(sys.argv[1], "r")
stats = f.read()
f.close()

stats = stats.split("\n")[:-1]

# pp(stats)
stats = list(map(lambda x: x.split(",") , stats))
print(str(len(stats)) + " kenken's processed")
df = pd.DataFrame(stats)
writer = pd.ExcelWriter(f'stats/{sys.argv[2]}.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer._save()