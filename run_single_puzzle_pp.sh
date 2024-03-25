#!/bin/bash
python3 kenken2smt.py <${1} >tmp/puz.smt
./mathsat -stats <tmp/puz.smt >tmp/model.smt
python3 smt2kenken.py tmp/model.smt tmp/stats.txt >tmp/result.txt --pretty